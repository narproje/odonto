angular.module('opal.services').factory('Fp17ODateOfCompletion', function(toMomentFilter, dateConflictCheck){
  /*
  * Date of completion is required if there is a completion type.
  * This is implied by the documentation from
  * "Mandatory item on form 2 of active treatment"
  *
  * Also it cannot be in the future.
  */

  return function(editing, step){
    "use strict";
    var completion_type = editing.orthodontic_treatment.completion_type;
    var dateOfCompletion = toMomentFilter(editing.orthodontic_treatment.date_of_completion);
    var assessment = editing.orthodontic_assessment;

    if(completion_type && completion_type.length){
      if(!dateOfCompletion){
        return {
          orthodontic_treatment: {
            date_of_completion: "Date of completion or last visit is required when there is a completion type"
          }
        }
      }
    }

    if(dateOfCompletion){
      if(dateOfCompletion > moment()){
        return {
          orthodontic_treatment: {
            date_of_completion: "Date of completion or last visit cannot be in the future"
          }
        }
      }

      // look at the range of dates betwen the beginning of the episode and the end
      // and make sure they don't overlap another episode
      // if the startDate is null that's fine dateConflictCheck will clean it out.
      var startDate = assessment.date_of_assessment || assessment.date_of_appliance_fitted;

      if(dateConflictCheck([startDate, dateOfCompletion], step.overlapping_dates)){
        return {
          orthodontic_treatment: {
            date_of_completion: "The FP17O overlaps with another FP17O of this patient"
          }
        }
      }
    }
  }
});