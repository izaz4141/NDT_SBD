import{i as b,r as d,l as I,o as a,c as l,b as e,F as C,g as D,t as i,w as V,v as M,n as B,d as k,f as A,q as $,m as U,I as T,k as f,s as q,x as z,y as O,z as K,A as R}from"./index.34fa7206.js";const G={class:"my-6"},H={class:"flex flex-col justify-center m-auto"},J=e("thead",{class:"w-full"},[e("tr",{class:"flex justify-around"},[e("th",{class:"w-[10vw]",scope:"col"},"Id"),e("th",{class:"w-[10vw]",scope:"col"},"Nama"),e("th",{class:"w-[10vw]",scope:"col"},"Email"),e("th",{class:"w-[9vw]",scope:"col"},"Author Level"),e("th",{class:"w-[15vw]",scope:"col"},"Pemesanan"),e("th",{class:"w-[10vw]",scope:"col"},"Departemen"),e("th",{class:"w-[15vw]",scope:"col"},"Peminjaman"),e("th",{class:"w-[15vw]",scope:"col"},"Pekerjaan"),e("th",{class:"w-[10vw]",scope:"col"},"Tanggal Daftar"),e("th",{class:"w-[20vw]",scope:"col"},"Actions")])],-1),Q={scope:"row",class:"w-[10vw] overflow-auto flex items-center justify-center"},W=["onClick"],X={class:"w-[10vw] overflow-auto"},Y={class:"w-[10vw] overflow-auto"},Z={class:"w-[9vw] justify-center flex items-center overflow-auto"},ee={key:0},te={key:1},se={class:"w-[15vw] justify-center flex items-center overflow-auto"},oe={class:"w-[10vw] justify-center flex items-center overflow-auto"},ae={key:0},le=["value"],ne={class:"w-[15vw] justify-center flex items-center overflow-auto"},re={class:"w-[15vw] justify-center flex items-center overflow-auto"},ce={key:0},ue=["value"],de={class:"w-[10vw] justify-center flex items-center overflow-auto"},ie={class:"w-[20vw] justify-center flex items-center overflow-auto"},ve={class:"flex gap-2 justify-center items-center"},_e=["onClick"],pe=["onClick"],we=["onClick"],he={__name:"TabelDaftarUsers",setup(E){const j=b("currentColor"),c=b("user"),h=b("data_dev_users"),n=d({}),v=d(""),_=d(""),p=d(""),m=d([]),x=d([]);function u(t){const r=["0","1","2","3","4","5","6","7","8","9","+"],o=t.key;r.includes(o)||t.preventDefault()}const y=t=>{n.value={},n.value[t.id]=!0,v.value=t.author_level,t.pekerjaan.id?p.value=t.pekerjaan.id:p.value="bukan",t.departemen?_.value=t.departemen.id:_.value="bukan"},w=()=>{n.value={}},g=async t=>{try{await f.post("/edit_user_dev",{user_id:t,dev_author_level:c.value.author_level,author_level:parseInt(v.value),departemen_id:_.value,pekerjaan_id:p.value}),await S(),n.value={}}catch(r){console.log(r)}},L=async t=>{try{await f.post("/remove_user",{user_id:t,author_level:c.value.author_level}),await S()}catch(r){console.log(r)}},S=async()=>{if(c.value)try{const t=await f.post("/dev_users_list",{author_level:c.value.author_level});h.value=t.data}catch(t){console.log(t)}else router.push("/")},N=async()=>{if(c.value)try{const t=await f.post("/pemesanan_list",{author_level:c.value.author_level});m.value=t.data}catch(t){console.log(t)}else router.push("/")},P=async()=>{try{const t=await f.get("/departemen_list");x.value=t.data}catch(t){console.log(t)}},F=t=>{navigator.clipboard.writeText(t)};return I(async()=>{await N(),await P()}),(t,r)=>(a(),l("div",G,[e("table",H,[J,e("tbody",null,[(a(!0),l(C,null,D(k(h),o=>(a(),l("tr",{key:o.id,class:"border-b border-gray-700 flex justify-around w-full items-center"},[e("th",Q,[e("button",{onClick:s=>F(o.id),class:"bg-sky-500 hover:bg-sky-400 text-white font-bold py-1 px-2 rounded-t"}," Copy ",8,W)]),e("td",X,[e("div",null,i(o.name),1)]),e("td",Y,[e("div",null,i(o.email),1)]),e("td",Z,[n.value[o.id]?(a(),l("div",ee,[V(e("input",{type:"text","onUpdate:modelValue":r[0]||(r[0]=s=>v.value=s),class:"w-[6vw] px-[1vw] py-1 bg-white dark:bg-gray-900 rounded-md border-1 text-center",style:B({borderColor:k(j)}),onKeypress:u},null,36),[[M,v.value]])])):(a(),l("div",te,i(o.author_level),1))]),e("td",se,[e("div",null,i(o.pesanan.map(s=>s.layanan).join(", ")),1)]),e("td",oe,[n.value[o.id]?(a(),l("div",ae,[V(e("select",{class:"px-4 py-1 bg-white dark:bg-gray-900 rounded-md border-1","onUpdate:modelValue":r[1]||(r[1]=s=>_.value=s)},[(a(!0),l(C,null,D(x.value,s=>(a(),l("option",{value:s.id},i(s.name),9,le))),256))],512),[[A,_.value]])])):$("",!0)]),e("td",ne,[e("div",null,i(o.meminjam.map(s=>s.item).join(", ")),1)]),e("td",re,[n.value[o.id]?(a(),l("div",ce,[V(e("select",{class:"px-4 py-1 bg-white dark:bg-gray-900 rounded-md border-1","onUpdate:modelValue":r[2]||(r[2]=s=>p.value=s)},[(a(!0),l(C,null,D(m.value,s=>(a(),l("option",{value:s.id},i(s.lokasi),9,ue))),256))],512),[[A,p.value]])])):$("",!0)]),e("td",de,i(o.date_added),1),e("td",ie,[e("div",ve,[n.value[o.id]?(a(),l("button",{key:0,onClick:s=>g(o.id),class:"bg-green-500 hover:bg-green-400 text-white font-bold py-1 px-4 rounded-t"}," Save ",8,_e)):(a(),l("button",{key:1,onClick:s=>y(o),class:"bg-blue-500 hover:bg-blue-400 text-white font-bold py-1 px-4 rounded-t"}," Edit ",8,pe)),e("button",{onClick:s=>L(o.id),class:"bg-red-500 hover:bg-red-400 text-white font-bold py-1 px-4 rounded-t"}," Delete ",8,we),n.value[o.id]?(a(),l("button",{key:2,onClick:w,class:"text-3xl rounded-full h-min w-min absolute right-2"},[U(k(T),{icon:"ic:twotone-cancel"})])):$("",!0)])])]))),128))])])]))}},ye={class:"flex flex-col justify-center my-12 text-center md:text-sm text-xs"},fe=e("h1",null,"Daftar User",-1),be={__name:"DevUserList",setup(E){const j=q(),c=d([]),h=d([]),n=d(""),v=b("user"),_=b("currentColor");z("data_dev_users",h);const p=(u,y)=>u.filter(w=>Object.keys(w).some(g=>typeof w[g]=="string"&&w[g].toLowerCase().includes(y.toLowerCase()))),m=()=>{const u=p(c.value,n.value);h.value=u},x=async()=>{if(v.value)try{const u=await f.post("/dev_users_list",{author_level:v.value.author_level});c.value=u.data}catch(u){console.log(u)}else j.push("/")};return O(async()=>{await x(),h.value=c.value}),K(c,()=>{m()},{deep:!0}),(u,y)=>(a(),l("div",ye,[fe,U(R,{searchClass:"w-[24rem] h-10 pl-8 pr-2 rounded-lg",modelValue:n.value,"onUpdate:modelValue":y[0]||(y[0]=w=>n.value=w),inputClass:"text-sm md:text-base",submitFunc:m,class:"m-auto my-4",style:B({borderColor:k(_)})},null,8,["modelValue","style"]),U(he)]))}};export{be as default};