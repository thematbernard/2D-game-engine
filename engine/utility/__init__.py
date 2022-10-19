def make_counter_action():
    import engine.utility.action.counter_increment as ci
    return ci.CounterIncrementAction()

def make_counter_entity(number):
    import engine.utility.entity.counter as count
    counter = count.Counter(number)
    return counter

def make_timer_entity(a_t, s_t, c_t, e_t):
    import engine.utility.entity.timer as timer
    myTimer = timer.Timer(a_t, s_t, c_t, e_t)
    return myTimer

def make_start_timer_action():
    import engine.utility.action.start_timer as st
    return st.StartTimerAction()

def make_alarm(a_time):
    import engine.utility.action.alarm as A
    return A.Alarm(a_time)

def update_action():
    import engine.utility.action.updateaction as ua
    return ua.UpdateAction()

def activate_action():
    import engine.utility.action.activate_entity as ae
    return ae.ActivateEntityAction()

def deactivate_action():
    import engine.utility.action.deactivate_entity as de
    return de.DeactivateEntityAction()