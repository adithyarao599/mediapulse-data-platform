class QualityScore:

    @staticmethod
    def calculate(total_rows, duplicate_rows, null_cells):

        deductions = duplicate_rows + null_cells

        score = max(0, ((total_rows - deductions) / total_rows) * 100)

        return round(score, 2)
