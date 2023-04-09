import requests

# URL deployed on my server
# baseUrl = "http://78.27.202.55:8000/"

# URL on localhost (Docker)
baseUrl = 'http://localhost:8000/'


# @pytest.fixture
def get_access_token(mail, password):
    """ GET access token for registered users/employee
    :param mail: mail user
    :param password: current password
    :return: access token
    """
    path = 'api/v1/token/'
    data_login = {'email': mail, "password": password}
    response = requests.post(baseUrl + path, data_login)
    access_employee = response.json()['access']
    print('acc', access_employee)
    return access_employee


def test_create_employee():
    path = 'api/v1/user/'
    data = {
        "email": "11employee_pytes@mail.ua",
        "first_name": "employee1",
        "last_name": "lst_name",
        "password": "admin"
    }
    response = requests.post(baseUrl + path, data)
    assert response.status_code == 201
    assert response.json()['email'] == "11employee_pytes@mail.ua"


def test_login_get_menu_token_employee():
    """Getting current day menu, using Authorization. Only for employee"""
    # get access token
    access_token_employee = get_access_token("employee_pytest1_@mail.ua", 'admin')
    # Get current day Menu
    endpoint = 'api/v1/menu_for_today/'
    headers = {'Authorization': 'Bearer ' + access_token_employee}
    response = requests.get(headers=headers, url=baseUrl + endpoint)
    assert response.status_code == 200


def test_list_users_exist():
    """Get all list of users, but checking length data first user[0]. As count of all users is variable"""
    path = 'api/v1/user/'
    response = requests.get(baseUrl + path)
    assert response.status_code == 200
    assert len(response.json()[0]) == 5
