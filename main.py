from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <div class="container">
    <header class="text-center text-light my-4">
      <h1 class="mb-4">Todo List</h1>
      <form class="search">
        <input class="form-control m-auto" type="text" name="search" placeholder="search todos" />
      </form>
    </header>  
    <ul class="list-group todos mx-auto text-light">
      <li class="list-group-item d-flex justify-content-between align-items-center">
        <span>play mariokart</span>
        <span class="delete">×</span>
      </li>
      <li class="list-group-item d-flex justify-content-between align-items-center">
        <span>defeat ganon in zelda</span>
        <span class="delete">×</span>
      </li>
      <li class="list-group-item d-flex justify-content-between align-items-center">
        <span>make a veggie pie</span>
        <span class="delete">×</span>
      </li>
    </ul>

    <form class="add text-center my-4">
      <label class="text-light">Add a new todo...</label>
      <input class="form-control m-auto" type="text" name="add" />
    </form>  
  
    </div>
    """