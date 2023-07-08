<script>
    import { page } from "$app/stores";

    let currentPath = $page.url.search;

    const sources = [
        { name: "Krebs", route: "?krebs" },
        { name: "THN", route: "?thn" },
        { name: "CISA", route: "?cisa" },
        { name: "SecWeek", route: "?secweek" },
    ];

    function updateRouteInfo(source) {
        currentPath = source.route;
    }

</script>

<div class="SourceSelector">
    {#each sources as source}
        <a
            href="/news{source.route}"
            class="SourceSelector__source
        {source.route === currentPath && 'selected'}"
            on:click={() => {
                updateRouteInfo(source);
            }}>{source.name}</a
        >
    {/each}
</div>

<style lang="scss">
    .SourceSelector {
        grid-column: 1/21;
        grid-row: 2/4;
        display: flex;
        display: -ms-flexbox;
        display: -webkit-flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        overflow-x: scroll;

        @media screen and (max-width: 415px) {
            width: 90%;
            margin: auto;
            justify-content: flex-start;
        }

        .SourceSelector__source {
            margin: auto;
            color: rgb(102, 102, 102);
            text-decoration: none;
            font-family: $primaryFont;
            font-size: 1.5rem;
            margin-left: 1rem;
            margin-right: 1rem;
        }

        .selected {
            color: white;
        }
    }
</style>
