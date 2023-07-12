<script>
    import Form from "$lib/Auth/Form/+page.svelte";
    const inputs = [
        {id:1, name:'username', placeholder:'Enter Username', type:'text'},
        {id:2, name:'password', placeholder:'Enter Password', type:'password'},
    ]
    const btnText = "Sign In"
</script>

<Form title="login" inputs={inputs} btnText={btnText}/>