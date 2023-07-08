<script>
    import SourceCard from "$lib/Main/SourceCard/+page.svelte";
    import SourceSelector from "$lib/News/SourceSelector/+page.svelte"
</script>


<div class="SourcesContainer">
    <SourceSelector />
    <div class="Sources">
        <SourceCard source={{logo:3, type:'Krebs' }} />
        <SourceCard source={{logo:3, type:'Krebs' }} />
        <SourceCard source={{logo:3, type:'Krebs' }} />
    </div>
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
    
        .Sources{
            overflow-y: hidden;
            grid-column: 1/21;
            grid-row: 4/21;
            height: 100%;
            width:100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            overflow-x: scroll;
        }

    }
 
</style>