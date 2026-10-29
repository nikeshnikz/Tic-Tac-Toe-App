class CorroptionError(Exception) :
    pass
try :
    raise CorroptionError("This election is corrupted")

except CorroptionError as e  :
    print(f"This election  is fraud : {e}")
