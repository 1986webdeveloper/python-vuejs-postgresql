var PersonListing = Vue.extend({
    template: '#person-listing-template',
    data: function() {
        return {
            users:[],
            searchQuery: ''
        }
    },
    created: function(){
        this.loading='true';
    this.$http.get("http://localhost:5000/api/v1/users.json")
            .then(response => {
                this.loading = false;
                this.users = response.body.data;
            })
            console.log('help');
    },
    methods:{
        deletePerson: function(person, index) {
            var self = this;
            console.log(person._id);
            swal({
                title: "Are you sure?",
                text: "Are you sure that you want to delete this record?",
                type: "warning",
                showCancelButton: true,
                showLoaderOnConfirm: true,
                preConfirm: function() {
                    $.ajax({
                        url: "http://localhost:5000/api/v1/users/" + person.id + ".json",
                        type: "DELETE"
                    })
                    return new Promise(function(resolve) {
                        setTimeout(function() {
                            resolve();
                        }, 5000);
                    });
                }
            }).then(function() {
                self.users.splice(index, 1);
                        swal('Record Deleted');
            });
        },
    }

});

var PersonCreation = Vue.extend({
        template: '#person-creation-template',
        data: function () {
            return {personFirstName: '', personLastName: '', personDob: '', zipCode: '' }
        },
         mounted() {
            $("#personDob").datepicker().on(
     		"changeDate", () => {this.personDob = $('#personDob').val()}
		);
        },
        methods: {
            createPersons: function() {
                this.$validator.validateAll().then(() => {
                    // eslint-disable-next-line
                    swal({
                        title: 'Record Added',
                        type: 'success',
                    });
                    this.$http.post("http://localhost:5000/api/v1/users.json", {
                        "data": {
                        "type": "users",
                        "attributes": {
                            firstname: this.personFirstName,
                            lastname:this.personLastName,
                            dob:this.personDob,
                            zipcode:this.zipCode
     
                        }
                    }

                    }, function(data) {
                        return false;
                    });
                }).catch(() => {
                });
            }
        }
});
        
var PersonUpdate = Vue.extend({
        template: '#person-detail-template',
        data: function () {
            return {personFirstName: '', personLastName: '', personDob: '', zipCode: '', sproduct:'' }
        },
        mounted() {
            $("#personDob").datepicker().on(
     		"changeDate", () => {this.personDob = $('#personDob').val()}
		);
        },
        created: function(){
            this.$http.get("http://localhost:5000/api/v1/users/" + this.$route.params.id + ".json")
            .then(response => {
                    this.sproduct = response.body.data.attributes;
                    this.personFirstName = this.sproduct.firstname;
                    this.personLastName = this.sproduct.lastname;
                    this.personDob = this.sproduct.dob;
                    this.zipCode = this.sproduct.zipcode;
                });
            },
            methods: {
                updatePerson: function () {
                    var temp_data = this.sproduct;
                    swal({
                            title: 'Record Updated',
                            type: 'success',
                    });
                    this.$http.put("http://localhost:5000/api/v1/users/" + this.$route.params.id + ".json", {
                    "data": {
                        "type": "users",
                        "attributes": {
                            firstname: this.personFirstName,
                            lastname:this.personLastName,
                            dob:this.personDob,
                            zipcode:this.zipCode
     
                        }
                    }
                    },function(data) {
                        console.log(data);
                    });
                }
            }
        });

var router = new VueRouter({
    mode: 'hash',
    base: window.location.href,
    routes: [
        {path: '/', component: PersonListing},
        {path: '/create', component: PersonCreation},
        {name: 'person', path: '/:id', component: PersonUpdate }
    ]
});

var app = new Vue({
    router
}).$mount('#app');
