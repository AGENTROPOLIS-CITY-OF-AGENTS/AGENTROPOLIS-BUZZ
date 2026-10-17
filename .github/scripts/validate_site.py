#!/usr/bin/env python3
"""Validate a static site directory: well-formed HTML, resolvable local links, no large light blocks."""

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

VOID = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}


class Checker(HTMLParser):
    def __init__(self, path: Path, root: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.path = path
        self.root = root
        self.stack: list[str] = []
        self.errors: list[str] = []
        self.ids: set[str] = set()
        self.fragments: list[tuple[Path, str]] = []
        self.has_lang = False
        self.has_viewport = False
        self.has_title = False
        self.has_main = False
        self.has_h1 = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        if tag == "html" and a.get("lang"):
            self.has_lang = True
        if tag == "meta" and a.get("name") == "viewport":
            self.has_viewport = True
        if tag == "title":
            self.has_title = True
        if tag == "main":
            self.has_main = True
        if tag == "h1":
            self.has_h1 = True
        if tag == "img" and "alt" not in a:
            self.errors.append(f"line {self.getpos()[0]}: <img> without alt")
        if a.get("id"):
            self.ids.add(a["id"])
        for key in ("href", "src"):
            if key in a and a[key]:
                self.check_link(a[key])
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"line {self.getpos()[0]}: unexpected </{tag}> (open: {self.stack[-3:]})")
            if tag in self.stack:
                while self.stack and self.stack.pop() != tag:
                    pass
        else:
            self.stack.pop()

    def check_link(self, href: str) -> None:
        parts = urlsplit(href)
        if parts.scheme in ("http", "https", "mailto") or href.startswith("//"):
            if parts.scheme == "http":
                self.errors.append(f"line {self.getpos()[0]}: insecure http link {href}")
            return
        if parts.scheme:
            return
        if not parts.path:
            if parts.fragment:
                self.fragments.append((self.path, parts.fragment))
            return
        if parts.path.startswith("/"):
            self.errors.append(
                f"line {self.getpos()[0]}: root-relative link {href} breaks under a project Pages base path; use a relative path"
            )
            return
        target = (self.path.parent / parts.path).resolve()
        if target.is_dir():
            target = target / "index.html"
        if not target.exists():
            self.errors.append(f"line {self.getpos()[0]}: broken local link {href}")
        elif parts.fragment and target.suffix == ".html":
            self.fragments.append((target, parts.fragment))

    def finish(self, ids_by_page: dict[Path, set[str]]) -> list[str]:
        if self.stack:
            self.errors.append(f"unclosed tags: {self.stack}")
        for target, frag in self.fragments:
            if frag not in ids_by_page.get(target, set()):
                where = "" if target == self.path else f" in {target.relative_to(self.root)}"
                self.errors.append(f"missing anchor target #{frag}{where}")
        for ok, msg in (
            (self.has_lang, "<html lang> missing"),
            (self.has_viewport, "viewport meta missing"),
            (self.has_title, "<title> missing"),
            (self.has_main, "<main> landmark missing"),
            (self.has_h1, "<h1> missing"),
        ):
            if not ok:
                self.errors.append(msg)
        return self.errors


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    pages = sorted(p.resolve() for p in root.rglob("*.html"))
    if not pages:
        print(f"no HTML files under {root}")
        return 1
    checkers: list[Checker] = []
    for page in pages:
        checker = Checker(page, root)
        checker.feed(page.read_text(encoding="utf-8"))
        checker.close()
        checkers.append(checker)
    ids_by_page = {c.path: c.ids for c in checkers}
    failed = False
    for checker in checkers:
        page = checker.path
        errors = checker.finish(ids_by_page)
        rel = page.relative_to(root)
        if errors:
            failed = True
            print(f"FAIL {rel}")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"ok   {rel}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
