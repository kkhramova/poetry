from __future__ import annotations


from poetry.vcs.git.backend import is_revision_sha, annotated_tag, GitRefSpec

VALID_SHA = "c5c7624ef64f34d9f50c3b7e8118f7f652fddbbd"


def test_invalid_revision_sha() -> None:
    result = is_revision_sha("invalid_input")
    assert result is False


def test_valid_revision_sha() -> None:
    result = is_revision_sha(VALID_SHA)
    assert result is True


def test_invalid_revision_sha_min_len() -> None:
    result = is_revision_sha("c5c7")
    assert result is False


def test_invalid_revision_sha_max_len() -> None:
    result = is_revision_sha(VALID_SHA + "42")
    assert result is False


def test_annotated_tag_with_string_input() -> None:
    result = annotated_tag("c5c7624ef64f3")
    assert result == b"c5c7624ef64f3^{}"


def test_annotated_tag_with_bytes_input() -> None:
    result = annotated_tag(b"c5c7624ef64f3")
    assert result == b"c5c7624ef64f3^{}"

