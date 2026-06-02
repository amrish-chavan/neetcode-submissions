Select u.name, case when count(r.user_id)>0 then sum(r.distance) else 0 end 
    as travelled_distance 
    from users u 
    left join rides r on r.user_id = u.id 
    group by u.name 
    order by travelled_distance Desc, u.name;