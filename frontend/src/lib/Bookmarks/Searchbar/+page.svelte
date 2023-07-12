<script>
    import { PUBLIC_API_URL } from "$env/static/public";
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();

    export let authToken;

    let searchQuery = null;



    async function findBookmark(event) {
        event.preventDefault();

        const response = await fetch(
            `${PUBLIC_API_URL}/api/bookmarks?title=${searchQuery}`,
            {
                method: "GET",
                headers: {
                    Authorization: `Bearer ${authToken}`,
                    Accept: "application/vnd.api+json",
                    "Content-Type": "application/vnd.api+json",
                },
            }
        );

        const data = await response.json();

        if (response.ok) {

            dispatch('foundSources', {
                sources: data
            })

        } else {
            displayError("Something Wrong");
        }
    }
</script>

<form class="BookmarksSearchbar" id=SearchForm>
    <input
        class="BookmarksSearchbar__input"
        type="text"
        bind:value={searchQuery}
    />
    <button class="BookmarksSearchbar__btn" form="SearchForm" on:click={findBookmark}>
        <i class="fa-solid fa-magnifying-glass"></i>
    </button >
</form>

<style lang="scss">
    .BookmarksSearchbar {
        grid-column: 1/21;
        grid-row: 2/4;
        padding: 0;
        display: flex;
        display: -ms-flexbox;
        display: -webkit-flex;
        align-items: center;
        justify-content: center;

        .BookmarksSearchbar__input {
            height: 100%;
            width: 12rem;
            padding: 0;
            background: rgb(36, 36, 36);
            border: none;
            outline: none;
            color: white;
            padding: 0 1rem 0 1rem;
            font-size: 1.3rem;

            border-top-left-radius: .5rem;
            border-bottom-left-radius: .5rem;

            @media screen and (max-width: 280px) {
                width: 50%;
            }
            &::placeholder {
                font-family: "Font Awesome 6 Free";
                font-weight: 900;
                font-size: 1.3rem;
            }
        }

        .BookmarksSearchbar__btn {
            height: 2.4rem;
            width: 2.5rem;
            border-top-right-radius: .5rem;
            border-bottom-right-radius: .5rem;
            color: white; 
            background: rgb(66, 66, 250);
            border: none;
        }
    }
</style>
