# pm.test("Status code is 201, created", function () {
#     pm.response.to.have.status(201);
# });
#
# var last_autor_id = pm.response.json().id;
# pm.environment.set("last_autor_id", last_autor_id); // save to ENV
# // var userID= users.data[users.data.length-1].id
# console.log('last_autor_id = ', last_autor_id)

# GET from postman tests
# var last_autor_id = pm.response.json().id;
# pm.environment.set("last_autor_id", last_autor_id); // save to ENV
# // var userID= users.data[users.data.length-1].id
# console.log('last_autor_id = ', last_autor_id)