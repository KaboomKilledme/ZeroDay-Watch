<script>
    import Form from "$lib/Auth/Form/+page.svelte";
    const inputs = [
        {id:1, name:'username', placeholder:'Create Username', type:'text'},
        {id:2, name:'password', placeholder:'Create Password', type:'password'},
        {id:3, name:'checkPassword', placeholder:'Confirm Password', type:'password'},
    ]
    const btnText = "Sign Up"
</script>

<Form title="register" inputs={inputs} btnText={btnText}/>