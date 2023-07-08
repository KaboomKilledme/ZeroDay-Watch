<script>
    
    import SourceCard from "$lib/Main/Sources/SourceCard/+page.svelte";

</script>

<div class="Sources">
    <SourceCard source={{logo:3, type:'Krebs' }} />
    <SourceCard source={{logo:3, type:'Krebs' }} />
    <SourceCard source={{logo:3, type:'Krebs' }} />
</div>


<style lang="scss">
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
</style>