import{_ as P,b as S,i as b,r as n,o as x,c as h,a as e,w as i,v as r,d as V,F,e as U,n as L,u as y,f as C,t as D,p as I,g as N}from"./index.092fe7e2.js";const o=d=>(I("data-v-5e56f0c0"),d=d(),N(),d),j={class:"my-12"},B=o(()=>e("h1",{class:"text-center justify-center flex mb-10 text-3xl font-extrabold"}," Pesan Layanan ",-1)),M=["onSubmit"],O={class:"form-row"},E=o(()=>e("label",{"html-for":"name",class:"form-label"},"Nama Lengkap",-1)),z={class:"div-input"},A={class:"form-row"},H=o(()=>e("label",{htmlFor:"email",class:"form-label"}," Email ",-1)),K={class:"div-input"},T={class:"form-row"},q=o(()=>e("label",{htmlFor:"text",class:"form-label"}," No Handphone ",-1)),G={class:"div-input"},J={class:"form-row"},Q=o(()=>e("label",{htmlFor:"text",class:"form-label"}," Lokasi ",-1)),R={class:"div-input"},W={class:"form-row"},X=o(()=>e("label",{htmlFor:"text",class:"form-label"}," Layanan ",-1)),Y=["value"],Z={class:"form-row"},$=o(()=>e("label",{htmlFor:"text",class:"form-label"}," Deskripsi Pekerjaan: ",-1)),ee={class:"div-input"},te={__name:"ProductOrderPage",setup(d){S(l=>({f769d4f0:y(f)}));const a=b("user"),f=b("currentColor"),u=n(a?a.value.name:""),c=n(a?a.value.email:""),m=n(a?a.value.no_telp:""),p=n(""),_=n(""),v=n(""),k=["gamma","xray","positron"],g=async()=>{try{await httpClient.post("/order",{name:u.value,email:c.value,no_telp:m.value,lokasi:p.value,layanan:_.value,deskripsi:v.value}),router.push("/")}catch(l){console.log(l)}};function w(l){const s=["0","1","2","3","4","5","6","7","8","9","+"],t=l.key;s.includes(t)||l.preventDefault()}return(l,s)=>(x(),h("div",j,[B,e("form",{onSubmit:C(g,["prevent"]),class:"text-center my-10 text-sm md:text-xl relative items-center pt-8 pl-8 pr-8 pb-2 centerer rounded-lg bg-slate-200 dark:bg-main-dark-bg"},[e("div",O,[E,e("div",z,[i(e("input",{type:"text",class:"form-input",id:"","onUpdate:modelValue":s[0]||(s[0]=t=>u.value=t)},null,512),[[r,u.value]])])]),e("div",A,[H,e("div",K,[i(e("input",{type:"email",class:"form-input",id:"","onUpdate:modelValue":s[1]||(s[1]=t=>c.value=t)},null,512),[[r,c.value]])])]),e("div",T,[q,e("div",G,[i(e("input",{type:"text",class:"form-input",id:"","onUpdate:modelValue":s[2]||(s[2]=t=>m.value=t),onKeypress:s[3]||(s[3]=t=>w(t))},null,544),[[r,m.value]])])]),e("div",J,[Q,e("div",R,[i(e("input",{type:"text",class:"form-input",id:"","onUpdate:modelValue":s[4]||(s[4]=t=>p.value=t)},null,512),[[r,p.value]])])]),e("div",W,[X,i(e("select",{class:"form-select","onUpdate:modelValue":s[5]||(s[5]=t=>_.value=t)},[(x(),h(F,null,U(k,t=>e("option",{value:t},D(t),9,Y)),64))],512),[[V,_.value]])]),e("div",Z,[$,e("div",ee,[i(e("textarea",{type:"text",class:"form-input min-h-[32vh] items-start",id:"","onUpdate:modelValue":s[6]||(s[6]=t=>v.value=t)},null,512),[[r,v.value]])])]),e("button",{type:"submit",class:"py-3 px-6 my-8 text-black dark:text-white font-semibold w-full",style:L({background:y(f)})}," Pesan ",4)],40,M)]))}},oe=P(te,[["__scopeId","data-v-5e56f0c0"]]);export{oe as default};