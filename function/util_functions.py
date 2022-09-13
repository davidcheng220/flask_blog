#getting id
def build_provider_obj(request, id):
    provider = {
        "id": id,
        "firstname": request.form['firstname'],
        "lastname": request.form['lastname'],
        "position": request.form['position'],
        "company": request.form['company'],
        }
    return provider

def getProviderIndex(id, providers_list):
    for i in range(0, len(providers_list)):
        if providers_list[i]['id'] == int(id):
            return i
    return None
