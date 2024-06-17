def GetDomain(email):
    div = email.split('@')

    return f"@{div[1]}"
    
print(GetDomain('user@domain.com'))