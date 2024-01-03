from flask import Flask, request
from utils.galleryUtils import getGallery, addgallery, deleteGallery
from utils.contactUtil import getContactus,addContact,updateContact
from utils.testimonialsUtils import getTestimonials,addTestimonial,updateTestimonial,deleteTestimonial
from utils.blogUtil import getBlogPosts,addBlogPost,updateBlogPost,deleteBlogPost
from utils.aboutUtil import get_aboutus,add_aboutus,update_aboutus
from utils.corouselUtil import get_corousels,add_corousel,update_corousel,delete_Coursel
from utils.productimagesUtil import get_product_images,add_product_image,update_product_image,delete_product_image
from utils.productPageUtil import get_product_pages,add_product_page,update_product_page,delete_product_page
from utils.servicePageUtil import get_service_pages,add_service_page,update_service_page,delete_service_page

app = Flask(__name__)

# Gallery API Starts
@app.route('/gallery')
def home():
    return getGallery()


# Route to handle POST requests to add a new student
@app.route('/gallery', methods=['POST'])
def add_student():
    return addgallery(request.get_json())


# Route to handle DELETE requests by ID
@app.route('/gallery/<int:gallery_id>', methods=['DELETE'])
def delete_gallery(gallery_id):
    return deleteGallery(gallery_id)

# Contact API starts
@app.route('/contactus')
def contactus():
    return getContactus()

@app.route('/contactus', methods=['POST'])
def addContacts():
    print(request.get_json())
    return addContact(request.get_json())

@app.route('/contactus/<int:contact_id>', methods=['PUT'])
def updateContacts(contact_id):
    print(request.get_json())
    return updateContact(request.get_json(),contact_id)


# Testimonial API's
@app.route('/testimonial')
def testimonial():
    return getTestimonials()

@app.route('/testimonial', methods=['POST'])
def addTestimonials():
    print(request.get_json())
    return addTestimonial(request.get_json())

@app.route('/testimonial/<int:id>', methods=['PUT'])
def updateTestimonials(id):
    print(request.get_json())
    return updateTestimonial(request.get_json(),id)

@app.route('/testimonial/<int:id>', methods=['DELETE'])
def deleteTestimonials(id):
    return deleteTestimonial(id)



# Blogs

@app.route('/blogs')
def blogs():
    return getBlogPosts()

@app.route('/blogs', methods=['POST'])
def addBlogs():
    print(request.get_json())
    return addBlogPost(request.get_json())

@app.route('/blogs/<int:id>', methods=['PUT'])
def updateBlogs(id):
    print(request.get_json())
    return updateBlogPost(request.get_json(),id)

@app.route('/blogs/<int:id>', methods=['DELETE'])
def deleteBlogs(id):
    return deleteBlogPost(id)

# About us

@app.route('/about')
def about():
    return get_aboutus()

@app.route('/about', methods=['POST'])
def addAbout():
    print(request.get_json())
    return add_aboutus(request.get_json())

@app.route('/about/<int:id>', methods=['PUT'])
def updateAbout(id):
    print(request.get_json())
    return update_aboutus(request.get_json(),id)


# Corousels

@app.route('/corousel')
def corousels():
    return get_corousels()

@app.route('/corousel', methods=['POST'])
def addCorousels():
    print(request.get_json())
    return add_corousel(request.get_json())

@app.route('/corousel/<int:id>', methods=['PUT'])
def updateCorousels(id):
    print(request.get_json())
    return update_corousel(request.get_json(),id)

@app.route('/corousel/<int:id>', methods=['DELETE'])
def deleteCorousels(id):
    return delete_Coursel(id)


# Product Images
@app.route('/pImages')
def productImages():
    return get_product_images()

@app.route('/pImages', methods=['POST'])
def addProductImages():
    print(request.get_json())
    return add_product_image(request.get_json())

@app.route('/pImages/<int:id>', methods=['PUT'])
def updateProductImages(id):
    print(request.get_json())
    return update_product_image(request.get_json(),id)

@app.route('/pImages/<int:id>', methods=['DELETE'])
def deleteProductImages(id):
    return delete_product_image(id)


# Product Pages
@app.route('/product')
def product():
    return get_product_pages()

@app.route('/product', methods=['POST'])
def addProduct():
    print(request.get_json())
    return add_product_page(request.get_json())

@app.route('/product/<int:id>', methods=['PUT'])
def updateProduct(id):
    print(request.get_json())
    return update_product_page(request.get_json(),id)

@app.route('/product/<int:id>', methods=['DELETE'])
def deleteProduct(id):
    return delete_product_page(id)

# Service Pages

@app.route('/sPage')
def services():
    return get_service_pages()

@app.route('/sPage', methods=['POST'])
def addServices():
    print(request.get_json())
    return add_service_page(request.get_json())

@app.route('/sPage/<int:id>', methods=['PUT'])
def updateServices(id):
    print(request.get_json())
    return update_service_page(request.get_json(),id)

@app.route('/sPage/<int:id>', methods=['DELETE'])
def deleteServices(id):
    return delete_service_page(id)

if __name__ == '__main__':
    app.run(debug=True)
