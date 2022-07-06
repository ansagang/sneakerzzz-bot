import configs

def adminCheck(data):
    if data.from_user.id in configs.admin_id:
        return True
    else:
        return False