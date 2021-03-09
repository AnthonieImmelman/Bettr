def not_in_past(value):
          """Return True if the given datetime is not in the past
          False otherwise.
          """
          now = datetime.now()
          if value < now:
              raise ValidationError("Date/Time is in the past!")
          return value
