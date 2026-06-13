from datetime import date


class AdvancedSCD:

    @staticmethod
    def expire_current_record(record):

        record.active_flag = False

        record.end_date = date.today()

        return record

    @staticmethod
    def create_new_record(record):

        record.active_flag = True

        record.effective_date = date.today()

        return record
