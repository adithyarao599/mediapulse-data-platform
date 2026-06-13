from app.core.session import SessionLocal


class BulkLoader:

    def load(self, dataframe, model):

        db = SessionLocal()

        try:

            records = dataframe.to_dict(orient="records")

            db.bulk_insert_mappings(model, records)

            db.commit()

        finally:

            db.close()
