<template>
  <div id="app">
    <base-wrapper></base-wrapper>
  </div>
</template>

<script>
import BaseWrapper from './components/BaseWrapper'

export default {
  name: 'app',
  components: {
    BaseWrapper
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
