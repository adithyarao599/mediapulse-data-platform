class KeyResolver:

    @staticmethod
    def resolve_key(lookup_dictionary, business_value):

        return lookup_dictionary.get(business_value)
