<template>
  <div class="container">
    <h3>Risks:</h3>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Id</th>
          <th scope="col">Name</th>
          <th scope="col">Description</th>
          <th scope="col">Active</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="risk in risks" v-bind:key="risk.id">
          <th scope="row">{{risk.id}}</th>
          <td>{{risk.name}}</td>
          <td>{{risk.description}}</td>
          <td>{{risk.active}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Risks',
  data () {
    return {
      risks: null
    }
  },
  created: function () {
    this.$axios.get('https://lmwnz8c0v3.execute-api.us-west-2.amazonaws.com/dev/insurance/risks/')
      .then(res => {
        this.risks = res.data
      })
  }
}
</script>

<style>
  h3 {
    margin-bottom: 5%;
  }
</style>
