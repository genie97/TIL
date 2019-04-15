<!--<template>-->
  <!--<div class="hello">-->
    <!--<h1>{{ msg }}</h1>-->
    <!--<h2>Essential Links</h2>-->
    <!--<ul>-->
      <!--<li>-->
        <!--<a-->
          <!--href="https://vuejs.org"-->
          <!--target="_blank"-->
        <!--&gt;-->
          <!--Core Docs-->
        <!--</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a-->
          <!--href="https://forum.vuejs.org"-->
          <!--target="_blank"-->
        <!--&gt;-->
          <!--Forum-->
        <!--</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a-->
          <!--href="https://chat.vuejs.org"-->
          <!--target="_blank"-->
        <!--&gt;-->
          <!--Community Chat-->
        <!--</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a-->
          <!--href="https://twitter.com/vuejs"-->
          <!--target="_blank"-->
        <!--&gt;-->
          <!--Twitter-->
        <!--</a>-->
      <!--</li>-->
      <!--<br>-->
      <!--<li>-->
        <!--<a-->
          <!--href="http://vuejs-templates.github.io/webpack/"-->
          <!--target="_blank"-->
        <!--&gt;-->
          <!--Docs for This Template-->
        <!--</a>-->
      <!--</li>-->
    <!--</ul>-->
    <!--<h2>Ecosystem</h2>-->
    <!--<ul>-->
      <!--<li>-->
        <!--<a-->
          <!--href="http://router.vuejs.org/"-->
          <!--target="_blank"-->
        <!--&gt;-->
          <!--vue-router-->
        <!--</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a-->
          <!--href="http://vuex.vuejs.org/"-->
          <!--target="_blank"-->
        <!--&gt;-->
          <!--vuex-->
        <!--</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a-->
          <!--href="http://vue-loader.vuejs.org/"-->
          <!--target="_blank"-->
        <!--&gt;-->
          <!--vue-loader-->
        <!--</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a-->
          <!--href="https://github.com/vuejs/awesome-vue"-->
          <!--target="_blank"-->
        <!--&gt;-->
          <!--awesome-vue-->
        <!--</a>-->
      <!--</li>-->
    <!--</ul>-->
  <!--</div>-->
<!--</template>-->

<!--<script>-->
<!--export default {-->
  <!--name: 'HelloWorld',-->
  <!--data () {-->
    <!--return {-->
      <!--msg: 'Welcome to Your Vue.js App'-->
    <!--}-->
  <!--}-->
<!--}-->
<!--</script>-->

<!--&lt;!&ndash; Add "scoped" attribute to limit CSS to this component only &ndash;&gt;-->
<!--<style scoped>-->
<!--h1, h2 {-->
  <!--font-weight: normal;-->
<!--}-->
<!--ul {-->
  <!--list-style-type: none;-->
  <!--padding: 0;-->
<!--}-->
<!--li {-->
  <!--display: inline-block;-->
  <!--margin: 0 10px;-->
<!--}-->
<!--a {-->
  <!--color: #42b983;-->
<!--}-->
<!--</style>-->

<template>
  <div class="hello">
    <br>
    <h1 class="title">Marketing</h1> <!-- Page title -->

    <hr>

    <div class="columns">
  <div class="column is-one-third is-offset-one-third">
    <form v-on:submit.prevent="addTask"> <!-- v-on:submit.prevent="addTask" calls the function addTask on submit -->
      <h2 class="subtitle">Add task</h2>

      <div class="field">
        <label class="label">Description</label>
        <div class="control">
          <input class="input" type="text" v-model="description"> <!-- Connects this field to the description variable -->
        </div>
      </div>

      <div class="field">
        <label class="label">Status</label>
        <div class="control">
          <div class="select">
            <select v-model="status"> <!-- Connects this field to the status variable -->v
              <option value="0">To do</option>
              <option value="1">Done</option>
            </select>
          </div>
        </div>
      </div>

      <div class="field is-grouped">
        <div class="control">
          <button class="button is-link">Submit</button>
        </div>
      </div>
    </form>
  </div>
</div>

    <hr>

    <div class="columns">
  <div class="column is-half">
    <h2 class="subtitle">Todo</h2>

    <div class="todo">
      <div class="card" v-for="task in tasks" v-if="task.status == 0"> <!-- Loop through the tasks array, if status is 0 (to do) then we'll show it. -->
        <div class="card-content">
          <div class="content">
            {{ task.description }} <!-- Print the task's description here -->
          </div>
        </div>

        <footer class="card-footer">
          <!-- From -->
          <a class="card-footer-item">Done</a>
          <!-- To -->
          <a class="card-footer-item" v-on:click="setStatus(task.id)">Done</a>
        </footer>
      </div>
    </div>
  </div>

  <div class="column is-half">
    <h2 class="subtitle">Done</h2>

    <div class="done">
      <div class="card" v-for="task in tasks" v-if="task.status == 1"> <!-- Loop through the tasks array, if status is 1 (done) then we'll show it. -->
        <div class="card-content">
          <div class="content">
            {{ task.description }}
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
  </div>
</template>

<script>
  import axios from 'axios'
export default {
  name: 'Main',
  data () {
    return {
      tasks: [], // Array for holding the tasks
      description: '',
      status: 0
    }
  },
  mounted () { // This will be called when HelloWorld is loaded
    this.getTasks(); // Call our getTasks function below
  },
  methods: {
    getTasks() {
        axios({
            method:'get',
            url: 'http://127.0.0.1:8000/tasks/',
            auth: {
                username: 'admin',
                password: 'admin123!'
            }
        }).then(response => this.tasks = response.data);
    },

    addTask() { // Function
  if (this.description) { // Check if the description is empty
    axios({
      method:'post',
      url: 'http://127.0.0.1:8000/tasks/',
      data: { // Send description and status to the server
        description: this.description,
        status: this.status
      },
      auth: { // Basic authentication
        username: 'admin',
        password: 'admin123!'
      }
    }).then((response) => {
      let newTask = {'id': response.data.id, 'description': this.description, 'status': parseInt(this.status)}

      this.tasks.push(newTask)

      this.description = '' // Reset description
      this.status = 0 // Reset status
    })
    .catch((error) => {
      console.log(error);
    });
  }
},
    setStatus(task_id) {
  let description = '';

  for (let i = 0; i < this.tasks.length; i++) {
    if (this.tasks[i].id === task_id) {
      this.tasks[i].status = 1
      description = this.tasks[i].description

      break
    }
  }

  axios({
    method:'put',
    url: 'http://127.0.0.1:8000/tasks/' + task_id + '/',
    headers: {
      'Content-Type': 'application/json'
    },
    data: {
      description: description,
      status: 1
    },
    auth: {
      username: 'admin',
      password: 'admin123!'
    }
  })
}
  }
}
</script>

<style scoped>
.select, select { /* 100% width for the select */
  width: 100%;
}

.card { /* Adding some air under the tasks */
  margin-bottom: 25px;
}

.done { /* Make the done tasks a little bit transparent */
  opacity: 0.3;
}
</style>
