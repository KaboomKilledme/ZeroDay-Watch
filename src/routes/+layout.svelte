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
        background: $backgroundColour
    }

    .MainContainer{
        width: 80%;
        margin: auto;
        height: 100%;
    
    }
</style>