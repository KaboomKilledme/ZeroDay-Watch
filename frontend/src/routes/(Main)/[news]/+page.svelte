<script>
    import Sources from "$lib/Main/Sources/+page.svelte";
    import SourceSelector from "$lib/News/SourceSelector/+page.svelte"
</script>


<div class="NewsSourcesContainer">
    <SourceSelector />
    <Sources />
</div>


<style lang="scss">
    .NewsSourcesContainer{
        height: 100%;
        width: 100%;
        display: grid;
        display: -ms-grid;
        display: -moz-grid;
        grid-template-columns: repeat(20,1fr);
        grid-template-rows: repeat(20,1fr);
    }
 
</style>