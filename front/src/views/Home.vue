<template>
    <div>
        <Header/>
        <h1>Themes</h1>
        <br>

        <div class="w3-card-4" style="width: 80%; margin: 35px auto" v-for="t in themes.reverse()" :key="t.id">

            <header class="w3-container w3-blue-grey">
                <h3>{{t.title}}</h3>
            </header>

            <div class="w3-container" style="display: flex">

                <div  style="flex-grow: 1; border-right: 1px solid #999999; height: 100px">
                    <img  :src="t.picture" :alt="t.username" >
                    <p>{{t.date}} by <b>{{t.username}}</b></p>
                </div>
                <div style="flex-grow: 5; text-align: left; margin-left: 20px">
                    <p >{{t.content}}</p>
                </div>

            </div>
            <p>  <span style="color: blue">{{t.likes}}</span> <i class="fa fa-arrow-alt-circle-up" style="font-size:20px;color:blue"></i> | <i class="fa fa-arrow-alt-circle-down" style="font-size:20px;color:black"></i> <span style="color: black">{{t.dislikes}}</span>   </p>
            <a class="w3-button w3-block" style="background-color: grey" @click="editTheme(t.id)" v-show="admin">Edit</a>
            <button class="w3-button w3-block w3-grey" @click="viewTheme(t.id)">Show</button>

        </div>


    </div>
</template>

<script>

    import {mapActions, mapState} from 'vuex';
    import Header from "@/components/Header";
    export default {
        name: "Home",
        components: {
            Header
        },
        computed: {
            ...mapState(['themes', 'users'])
        },
        methods: {
            ...mapActions(['load_themes', 'load_users']),

            viewTheme : function (id) {
                this.$router.push({path: `/theme/${id}`})
            },
            seeUser: function (id) {

                this.$router.push({path: `../user/${id}`})

            },
            isAdmin: function () {
                if(localStorage.getItem('role') === 'admin'){
                    this.admin = true
                }else {
                    this.admin = false
                }
            },
            editTheme: function (id) {
                window.location = `http://localhost:8000/edit/${id}`
            }

        },
        mounted: function () {
            this.isAdmin()
            if(localStorage.getItem('auth') == null){
                this.$router.push('../log')
                return
            }
            this.load_themes()
            this.load_users()
        },
        data() {
            return {
                items:[
                    {msg: 'msg', mss: 'mss'},
                    {msg: 'msg2', mss: 'mss2'},
                    {msg: 'msg3', mss: 'mss3'}

                ],
                role: localStorage.getItem('role')

            }

        }

    }

    /*<div >
            <div class="w3-card-4 theme" style="width:80%;margin: 30px auto"  v-for="theme in themes" :key="theme.id">
                <header class="w3-container  w3-light-grey">

                    <h1><a @click="viewTheme(theme.id)">{{theme.title}}</a></h1>
                </header>

                <div class="w3-container">
                    <p>{{theme.content}}</p>
                </div>

                <footer class="w3-container  w3-light-grey">
                    <h5>{{theme.date.slice(0,10)}} by {{theme.username}}</h5>
                </footer>
            </div>
        </div>*/
</script>

<style scoped>
    @import "https://www.w3schools.com/w3css/4/w3.css";

    a{
        text-decoration: none;
        color: #000000;
        background-color: #b20000;
    }

    a:hover{
        cursor: pointer;
    }

    img{

        height: 80px;
        width: 80px;
        margin-top: 3px;

    }


</style>
