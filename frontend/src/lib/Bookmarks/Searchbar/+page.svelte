<div class="BookmarksSearchbar">
    <input class="BookmarksSearchbar__input" type="text" placeholder="&#xf002;">
</div>


<style lang="scss">
    .BookmarksSearchbar{
        grid-column:1/21;
        grid-row: 2/4;
        padding: 0;
        display: flex;
        display: -ms-flexbox;
        display: -webkit-flex;
        align-items: center;
        justify-content: center;

        .BookmarksSearchbar__input{
            height: 100%;
            width: 14rem;
            padding: 0;
            border-radius: 2rem;
            background: rgb(36, 36, 36);
            border: none;
            outline: none;
            color: white;
            padding: 0 1rem 0 1rem;
            font-size: 1.3rem;

            @media screen and (max-width:280px){
                width: 80%;
            }
            &::placeholder{
                font-family: 'Font Awesome 6 Free';
                font-weight: 900;
                font-size: 1.3rem;
                color: #00b5ec;
            }
        }
    }
</style>
