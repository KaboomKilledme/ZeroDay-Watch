<script>
    import Sources from "$lib/Main/Sources/+page.svelte";
    import SourceSelector from "$lib/News/SourceSelector/+page.svelte";
    import Content from "$lib/Main/Content/+page.svelte";

    let shownContent = null;

    let content;

    const secWeekTitle = "After Zero-Day Attacks, MOVEit Turns to Security Service Packs"
    const secWeekText = `
    `

    const krebsTitle = "Top Suspect in 2015 Ashley Madison Hack Committed Suicide in 2014"
    const krebsText = `
        `
    const THNtitle = 'Two Spyware Apps on Google Play with 1.5 Million Users Sending Data to China' ;
    const THNtext = `
        `

    const CISAtitle = 'CISA Announces Updates to the Election Security Team'
    const CISAtext = `
       `

    let sources = [
        {id:1, logo:1, type:'SecWeek', title:secWeekTitle, text:secWeekText},
        {id:2, logo:3, type:'Krebs', title:krebsTitle, text:krebsText},
        {id:3, logo:2, type:'THN', title:THNtitle, text:THNtext},
        {id:4, logo:4, type:'CISA', title:CISAtitle, text:CISAtext},
        {id:7, logo:1, type:'SecWeek', title:secWeekTitle, text:secWeekText},
        {id:8, logo:3, type:'Krebs', title:krebsTitle, text:krebsText},
        {id:9, logo:2, type:'THN', title:THNtitle, text:THNtext},
        {id:10, logo:4, type:'CISA', title:CISAtitle, text:CISAtext},
    ]

    function showContent(event){
        shownContent = event.detail.source.id
        if(shownContent !== null){
            content = event.detail.source
        }
    }

</script>


<div class="NewsSourcesContainer">
    <SourceSelector />
    <Sources sources={sources} on:showContent={showContent} />

    {#if shownContent}
        <Content content={content} on:close={showContent} />
    {/if}
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