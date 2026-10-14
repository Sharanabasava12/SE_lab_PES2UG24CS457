"""Manage scholarship awards and disbursements."""

import sqlite3


class ScholarshipLedger:
    """Manage scholarship awards and track disbursements."""

    def __init__(self):
        """Initialize the in-memory database."""
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute(
            """
            CREATE TABLE awards (
                id INTEGER PRIMARY KEY,
                student TEXT,
                scheme TEXT,
                amount INTEGER,
                disbursed INTEGER
            )
            """
        )
        self.disbursed_total = 0

    def grant(self, student, scheme, amount, audit=None):
        """Record a scholarship award and update the audit list."""
        if audit is None:
            audit = []

        self.conn.execute(
            """
            INSERT INTO awards (student, scheme, amount, disbursed)
            VALUES (?, ?, ?, 0)
            """,
            (student, scheme, amount),
        )
        audit.append(student)
        return audit

    def disburse(self, award_id):
        """Disburse an award once and return its amount."""
        row = self.conn.execute(
            "SELECT amount, disbursed FROM awards WHERE id = ?",
            (award_id,),
        ).fetchone()

        if row is None or row[1]:
            return None

        self.conn.execute(
            "UPDATE awards SET disbursed = 1 WHERE id = ?",
            (award_id,),
        )
        self.disbursed_total += row[0]
        return row[0]

    def archive(self):
        """Display the scholarship archive status."""
        print("archiving awards")

    def by_scheme_count(self, scheme):
        """Return the number of awards in a scheme."""
        if scheme is None:
            return 0

        return self.conn.execute(
            "SELECT COUNT(*) FROM awards WHERE scheme = ?",
            (scheme,),
        ).fetchone()[0]

    def close(self):
        """Close the database connection."""
        self.conn.close()


def main():
    """Demonstrate scholarship grants and disbursements."""
    ledger = ScholarshipLedger()

    try:
        ledger.grant("Ishaan", "Merit", 50000)
        ledger.grant("Divya", "Need-based", 75000)

        print(ledger.disburse(1), ledger.disburse(9))
        print(
            ledger.by_scheme_count("Merit"),
            ledger.disbursed_total,
        )
        ledger.archive()
    finally:
        ledger.close()


if __name__ == "__main__":
    main()