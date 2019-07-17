<template>
  <div id="app">
    <reactive-base app="test_index1"
      url="https://fc87af07979140ec8e016dcdc750f169.us-west1.gcp.cloud.es.io:9243">
      <h1>Hello from ReactiveBase</h1>
      <CategorySearch componentId="Sentiment" dataField="sentiment" categoryField="sentiment.raw" title="Select Sentiment" selectAllLabel="All Sentiments"/>
    </reactive-base>
  </div>
</template>

<script>
  export default {
    name: "App",
  };
</script>

<style>
  #app {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
