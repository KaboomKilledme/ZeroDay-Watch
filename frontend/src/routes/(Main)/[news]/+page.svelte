<script>
    import Sources from "$lib/Main/Sources/+page.svelte";
    import SourceSelector from "$lib/News/SourceSelector/+page.svelte"
</script>


<div class="SourcesContainer">
    <SourceSelector />
    <Sources />
</div>


<style lang="scss">
    .SourcesContainer{
        height: 100%;
        width: 100%;
        display: grid;
        display: -ms-grid;
        display: -moz-grid;
        grid-template-columns: repeat(20,1fr);
        grid-template-rows: repeat(20,1fr);
    
    
    }
 
</style>