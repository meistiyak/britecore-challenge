<template>
  <footer>
    <p>Copyright &copy; {{ cur_year }}</p>
  </footer>
</template>

<script>
export default {
  computed: {
    cur_year () {
      return new Date().getFullYear()
    }
  }
}
</script>

<style>
  footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    text-align: center;
    border-top: 1px solid #eaecef;
  }
  footer p {
      margin-left: 1rem;
  }
</style>
