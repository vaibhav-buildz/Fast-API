from fastapi import FastAPI, Request
from mockData import products
from dtos import ProductDTO

app = FastAPI()




@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI server!"}




@app.get("/products")
def get_products():
    # This function would typically fetch products from a database or another source
    return products
 



## path parameters
@app.get("/product/{product_id}")
def get_one_product(product_id: int):
    ## if producct available with the id then return the product else return error message
    

    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct


    return {
        "error": "Product not found"
        }




## query parameters

@app.get("/greet")
def greet_user(request: Request):
    query_params = dict(request.query_params)
    print(query_params)
    return {
        "greet": f"Hello, {query_params.get('name')}! Welcome to our API!, Your age is {query_params.get('age')}"
    }




## diffrent types of request methods

@app.post("/create_product")
def create_product(product_data: ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)
    return {"status": "Product created successfully", "product": product_data}




@app.put("/update_product/{product_id}")
def update_product(product_id: int, product_data: ProductDTO):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            return {"status": "Product updated successfully", "product": products[index]}
    return {"error": "Product not found"} 

 


@app.delete("/delete_product/{product_id}")
def delete_product(product_id: int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deleted_product = products.pop(index)
            return {"status": "Product deleted successfully", "product": deleted_product}
    return {"error": "Product not found"}





## how to validate data. - DTOS
## how to call different http methods - GET, POST, PUT, DELETE  