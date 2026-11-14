#!/usr/bin/env python3
# Scaffold a Java problem class and a JUnit test.
# Usage (from anywhere inside the repo):
#     python scripts/new_problem.py arrays ContainsDuplicate
import sys
from pathlib import Path

SOLUTION = """package dsa.{topic};

/**
 * {name}
 *
 * Link: TODO
 * Difficulty: TODO (Easy / Medium / Hard)
 *
 * Approach: TODO
 * Time: O(?)   Space: O(?)
 */
public class {name} {{

    public static Object solve(Object input) {{
        // TODO
        return null;
    }}

    public static void main(String[] args) {{
        System.out.println(solve(null));
    }}
}}
"""

TEST = """package dsa.{topic};

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class {name}Test {{

    @Test
    void basicCase() {{
        // TODO: replace with real assertions
        assertNull({name}.solve(null));
    }}
}}
"""


def main():
    if len(sys.argv) != 3:
        print("Usage: python scripts/new_problem.py <topic> <ClassName>")
        sys.exit(1)
    topic, name = sys.argv[1].lower(), sys.argv[2]
    repo = Path(__file__).resolve().parent.parent
    src = repo / "dsa" / "src" / "main" / "java" / "dsa" / topic / (name + ".java")
    tst = repo / "dsa" / "src" / "test" / "java" / "dsa" / topic / (name + "Test.java")
    for path, body in ((src, SOLUTION), (tst, TEST)):
        if path.exists():
            print("Already exists, skipping:", path)
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body.format(topic=topic, name=name), encoding="utf-8")
        print("Created", path.relative_to(repo))


if __name__ == "__main__":
    main()
