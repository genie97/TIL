<template>
  <div class="container">
    <div class="large-12 medium-12 small-12 cell">
      <label>File<br/>
        Project Name : <input type="text"><br/>
        Project File : <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
      </label>
      <br>
      <button v-on:click="submitFile()">Submit</button>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        file: ''
      }
    },
    methods: {
      submitFile() {
        let formData = new FormData();
        formData.append('file', this.file);

        axios.post('/upload/new',
          formData,
          {
            headers: {
              'content-type': 'multipart/form-data'
            }
          }
        ).then(function() {
          console.log('SUCCESS!!');
        })
          .catch(function() {
            console.log('FAILURE!!');
          });
      },
      handleFileUpload() {
        this.file = this.$refs.file.files[0];
      }
    }
  }
</script>
