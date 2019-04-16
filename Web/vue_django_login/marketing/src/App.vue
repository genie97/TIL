<template>
  <div id="app">
    <b-navbar toggleable="md" type="dark" variant="dark">

    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

    <b-navbar-brand href="#"><img src="./assets/logo.png" class="d-inline-block align-center " width=50px height=auto>Marketing AI</b-navbar-brand>

    <b-collapse is-nav id="nav_collapse">

      <b-navbar-nav>
        <b-nav-item href="#">reviews</b-nav-item>
        <b-nav-item href="#" disabled>Disabled</b-nav-item>
        <b-nav-item-dropdown right>
          <!-- Using button-content slot -->
          <template slot="button-content">
            <em>menu</em>
          </template>
          <b-dropdown-item href="#">drop</b-dropdown-item>
          <b-dropdown-item href="#">down</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
    <b-navbar-nav class="ml-auto">

        <b-nav-item-dropdown text="dropdown" right>
          <b-dropdown-item href="#">드</b-dropdown-item>
          <b-dropdown-item href="#">롭</b-dropdown-item>
          <b-dropdown-item href="#">다</b-dropdown-item>
          <b-dropdown-item href="#">운</b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" type="text" placeholder="Search"/>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>




          <div>
  <b-button @click="show=true" variant="primary" size="sm" class="my-2 my-sm-0">Sign In / Sign Up</b-button>

    <b-modal
      v-model="show"
      title="Sign In"
      :header-bg-variant="headerBgVariant"
      :header-text-variant="headerTextVariant"
      :body-bg-variant="bodyBgVariant"
      :body-text-variant="bodyTextVariant"
      :footer-bg-variant="footerBgVariant"
      :footer-text-variant="footerTextVariant"
    >
      <b-container fluid>
        <div>
          <b-row>
          <p class="float-left">E-mail:   </p>
          <b-form-input id="input-id" type="email" placeholder="Enter your email" />
            </b-row>
          <b-row>
          <p class="float-left">Password:   </p>
          <b-form-input type="password" placeholder="Enter your password" />
            </b-row>
        </div>

        <!--<b-row class="mb-1 text-center">-->
          <!--<b-col cols="3" />-->
          <!--<b-col>Background</b-col>-->
          <!--<b-col>Text</b-col>-->
        <!--</b-row>-->

        <!--<b-row class="mb-1">-->
          <!--<b-col cols="3">Header</b-col>-->
          <!--<b-col><b-form-select :options="variants" v-model="headerBgVariant" /></b-col>-->
          <!--<b-col><b-form-select :options="variants" v-model="headerTextVariant" /></b-col>-->
        <!--</b-row>-->

        <!--<b-row class="mb-1">-->
          <!--<b-col cols="3">Body</b-col>-->
          <!--<b-col><b-form-select :options="variants" v-model="bodyBgVariant" /></b-col>-->
          <!--<b-col><b-form-select :options="variants" v-model="bodyTextVariant" /></b-col>-->
        <!--</b-row>-->

        <!--<b-row>-->
          <!--<b-col cols="3">Footer</b-col>-->
          <!--<b-col><b-form-select :options="variants" v-model="footerBgVariant" /></b-col>-->
          <!--<b-col><b-form-select :options="variants" v-model="footerTextVariant" /></b-col>-->
        <!--</b-row>-->
      </b-container>

      <div slot="modal-footer" class="w-100">
        <p class="float-left">Modal Footer Content</p>
        <!--<b-button size="sm" class="float-right" variant="primary" @click="show=false">Close</b-button>-->
      <b-button size="sm" class="float-right" variant="primary" @click="show=false">Close</b-button>
        <b-button size="sm" class="float-right" variant="primary" @click="show=false">Sign in</b-button>

      </div>
    </b-modal>
</div>


        </b-nav-form>
    </b-navbar-nav>

      </b-collapse>
    </b-navbar>
    <router-view/>
  </div>
</template>


<script>
  import Vue from 'vue'
  import BootstrapVue from 'bootstrap-vue'
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'
  import ReactiveSearch from '@appbaseio/reactivesearch-vue'
  Vue.use(ReactiveSearch);
  Vue.use(BootstrapVue);
export default {
  name: 'App',
  data()
  {
    return {
        show: false,
        variants: ['primary', 'secondary', 'success', 'warning', 'danger', 'info', 'light', 'dark'],
        headerBgVariant: 'dark',
        headerTextVariant: 'light',
        bodyBgVariant: 'light',
        bodyTextVariant: 'dark',
        footerBgVariant: 'light',
        footerTextVariant: 'dark'
      }
  }
}
</script>





<style>
@import url('https://fonts.googleapis.com/css?family=Ubuntu');
#app {
  /*font-family: 'Avenir', Helvetica, Arial, sans-serif;*/
  font-family: 'Ubuntu', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
  .modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}
.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}
.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
}
.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}
.modal-body {
  margin: 20px 0;
}
.modal-default-button {
  float: right;
}
/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */
.modal-enter {
  opacity: 0;
}
.modal-leave-active {
  opacity: 0;
}
.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
