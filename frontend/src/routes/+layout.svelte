<script>

</script>

<svelte:head>
    <link rel="stylesheet" href="./src/styles/style.scss">
</svelte:head>

<div class="MainPage">
    <main class="MainContainer">
        <slot />
    </main>
</div>


<style lang="scss">
    .MainPage{
        width: 100%;
        padding:0;
        margin:0;
        background: $backgroundColour;
        overflow-y: hidden;
        overflow-x: hidden;
        overflow: hidden;

    }

    .MainContainer{
        display: flex;
        display: -ms-flexbox;
        display: -webkit-flex;
        flex-direction: column;
        margin: auto;
        height: 100%;
        padding: 0;
        overflow-y: scroll;

    
    }

   
</style>