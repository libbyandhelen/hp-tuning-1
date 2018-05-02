# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import pkg.api.python.api_pb2 as api__pb2


class ManagerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateStudy = channel.unary_unary(
        '/api.Manager/CreateStudy',
        request_serializer=api__pb2.CreateStudyRequest.SerializeToString,
        response_deserializer=api__pb2.CreateStudyReply.FromString,
        )
    self.StopStudy = channel.unary_unary(
        '/api.Manager/StopStudy',
        request_serializer=api__pb2.StopStudyRequest.SerializeToString,
        response_deserializer=api__pb2.StopStudyReply.FromString,
        )
    self.GetStudy = channel.unary_unary(
        '/api.Manager/GetStudy',
        request_serializer=api__pb2.GetStudyRequest.SerializeToString,
        response_deserializer=api__pb2.GetStudyReply.FromString,
        )
    self.GetStudyList = channel.unary_unary(
        '/api.Manager/GetStudyList',
        request_serializer=api__pb2.GetStudyListRequest.SerializeToString,
        response_deserializer=api__pb2.GetStudyListReply.FromString,
        )
    self.GetTrials = channel.unary_unary(
        '/api.Manager/GetTrials',
        request_serializer=api__pb2.GetTrialsRequest.SerializeToString,
        response_deserializer=api__pb2.GetTrialsReply.FromString,
        )
    self.GetTrial = channel.unary_unary(
        '/api.Manager/GetTrial',
        request_serializer=api__pb2.GetTrialRequest.SerializeToString,
        response_deserializer=api__pb2.GetTrialReply.FromString,
        )
    self.CreateTrial = channel.unary_unary(
        '/api.Manager/CreateTrial',
        request_serializer=api__pb2.CreateTrialRequest.SerializeToString,
        response_deserializer=api__pb2.CreateTrialReply.FromString,
        )
    self.UpdateTrial = channel.unary_unary(
        '/api.Manager/UpdateTrial',
        request_serializer=api__pb2.UpdateTrialRequest.SerializeToString,
        response_deserializer=api__pb2.UpdateTrialReply.FromString,
        )
    self.RunTrial = channel.unary_unary(
        '/api.Manager/RunTrial',
        request_serializer=api__pb2.RunTrialRequest.SerializeToString,
        response_deserializer=api__pb2.RunTrialReply.FromString,
        )
    self.StopWorkers = channel.unary_unary(
        '/api.Manager/StopWorkers',
        request_serializer=api__pb2.StopWorkersRequest.SerializeToString,
        response_deserializer=api__pb2.StopWorkersReply.FromString,
        )
    self.GetWorkers = channel.unary_unary(
        '/api.Manager/GetWorkers',
        request_serializer=api__pb2.GetWorkersRequest.SerializeToString,
        response_deserializer=api__pb2.GetWorkersReply.FromString,
        )
    self.GetSuggestions = channel.unary_unary(
        '/api.Manager/GetSuggestions',
        request_serializer=api__pb2.GetSuggestionsRequest.SerializeToString,
        response_deserializer=api__pb2.GetSuggestionsReply.FromString,
        )
    self.GetShouldStopWorkers = channel.unary_unary(
        '/api.Manager/GetShouldStopWorkers',
        request_serializer=api__pb2.GetShouldStopWorkersRequest.SerializeToString,
        response_deserializer=api__pb2.GetShouldStopWorkersReply.FromString,
        )
    self.GetMetrics = channel.unary_unary(
        '/api.Manager/GetMetrics',
        request_serializer=api__pb2.GetMetricsRequest.SerializeToString,
        response_deserializer=api__pb2.GetMetricsReply.FromString,
        )
    self.SetSuggestionParameters = channel.unary_unary(
        '/api.Manager/SetSuggestionParameters',
        request_serializer=api__pb2.SetSuggestionParametersRequest.SerializeToString,
        response_deserializer=api__pb2.SetSuggestionParametersReply.FromString,
        )
    self.GetSuggestionParameters = channel.unary_unary(
        '/api.Manager/GetSuggestionParameters',
        request_serializer=api__pb2.GetSuggestionParametersRequest.SerializeToString,
        response_deserializer=api__pb2.GetSuggestionParametersReply.FromString,
        )
    self.GetSuggestionParameterList = channel.unary_unary(
        '/api.Manager/GetSuggestionParameterList',
        request_serializer=api__pb2.GetSuggestionParameterListRequest.SerializeToString,
        response_deserializer=api__pb2.GetSuggestionParameterListReply.FromString,
        )
    self.SetEarlyStoppingParameters = channel.unary_unary(
        '/api.Manager/SetEarlyStoppingParameters',
        request_serializer=api__pb2.SetEarlyStoppingParametersRequest.SerializeToString,
        response_deserializer=api__pb2.SetEarlyStoppingParametersReply.FromString,
        )
    self.GetEarlyStoppingParameters = channel.unary_unary(
        '/api.Manager/GetEarlyStoppingParameters',
        request_serializer=api__pb2.GetEarlyStoppingParametersRequest.SerializeToString,
        response_deserializer=api__pb2.GetEarlyStoppingParametersReply.FromString,
        )
    self.SaveStudy = channel.unary_unary(
        '/api.Manager/SaveStudy',
        request_serializer=api__pb2.SaveStudyRequest.SerializeToString,
        response_deserializer=api__pb2.SaveStudyReply.FromString,
        )
    self.SaveModel = channel.unary_unary(
        '/api.Manager/SaveModel',
        request_serializer=api__pb2.SaveModelRequest.SerializeToString,
        response_deserializer=api__pb2.SaveModelReply.FromString,
        )
    self.GetSavedStudies = channel.unary_unary(
        '/api.Manager/GetSavedStudies',
        request_serializer=api__pb2.GetSavedStudiesRequest.SerializeToString,
        response_deserializer=api__pb2.GetSavedStudiesReply.FromString,
        )
    self.GetSavedModels = channel.unary_unary(
        '/api.Manager/GetSavedModels',
        request_serializer=api__pb2.GetSavedModelsRequest.SerializeToString,
        response_deserializer=api__pb2.GetSavedModelsReply.FromString,
        )


class ManagerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateStudy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopStudy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStudy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStudyList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTrials(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTrial(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateTrial(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateTrial(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RunTrial(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopWorkers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetWorkers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSuggestions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetShouldStopWorkers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMetrics(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetSuggestionParameters(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSuggestionParameters(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSuggestionParameterList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetEarlyStoppingParameters(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEarlyStoppingParameters(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SaveStudy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SaveModel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSavedStudies(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSavedModels(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ManagerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateStudy': grpc.unary_unary_rpc_method_handler(
          servicer.CreateStudy,
          request_deserializer=api__pb2.CreateStudyRequest.FromString,
          response_serializer=api__pb2.CreateStudyReply.SerializeToString,
      ),
      'StopStudy': grpc.unary_unary_rpc_method_handler(
          servicer.StopStudy,
          request_deserializer=api__pb2.StopStudyRequest.FromString,
          response_serializer=api__pb2.StopStudyReply.SerializeToString,
      ),
      'GetStudy': grpc.unary_unary_rpc_method_handler(
          servicer.GetStudy,
          request_deserializer=api__pb2.GetStudyRequest.FromString,
          response_serializer=api__pb2.GetStudyReply.SerializeToString,
      ),
      'GetStudyList': grpc.unary_unary_rpc_method_handler(
          servicer.GetStudyList,
          request_deserializer=api__pb2.GetStudyListRequest.FromString,
          response_serializer=api__pb2.GetStudyListReply.SerializeToString,
      ),
      'GetTrials': grpc.unary_unary_rpc_method_handler(
          servicer.GetTrials,
          request_deserializer=api__pb2.GetTrialsRequest.FromString,
          response_serializer=api__pb2.GetTrialsReply.SerializeToString,
      ),
      'GetTrial': grpc.unary_unary_rpc_method_handler(
          servicer.GetTrial,
          request_deserializer=api__pb2.GetTrialRequest.FromString,
          response_serializer=api__pb2.GetTrialReply.SerializeToString,
      ),
      'CreateTrial': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTrial,
          request_deserializer=api__pb2.CreateTrialRequest.FromString,
          response_serializer=api__pb2.CreateTrialReply.SerializeToString,
      ),
      'UpdateTrial': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateTrial,
          request_deserializer=api__pb2.UpdateTrialRequest.FromString,
          response_serializer=api__pb2.UpdateTrialReply.SerializeToString,
      ),
      'RunTrial': grpc.unary_unary_rpc_method_handler(
          servicer.RunTrial,
          request_deserializer=api__pb2.RunTrialRequest.FromString,
          response_serializer=api__pb2.RunTrialReply.SerializeToString,
      ),
      'StopWorkers': grpc.unary_unary_rpc_method_handler(
          servicer.StopWorkers,
          request_deserializer=api__pb2.StopWorkersRequest.FromString,
          response_serializer=api__pb2.StopWorkersReply.SerializeToString,
      ),
      'GetWorkers': grpc.unary_unary_rpc_method_handler(
          servicer.GetWorkers,
          request_deserializer=api__pb2.GetWorkersRequest.FromString,
          response_serializer=api__pb2.GetWorkersReply.SerializeToString,
      ),
      'GetSuggestions': grpc.unary_unary_rpc_method_handler(
          servicer.GetSuggestions,
          request_deserializer=api__pb2.GetSuggestionsRequest.FromString,
          response_serializer=api__pb2.GetSuggestionsReply.SerializeToString,
      ),
      'GetShouldStopWorkers': grpc.unary_unary_rpc_method_handler(
          servicer.GetShouldStopWorkers,
          request_deserializer=api__pb2.GetShouldStopWorkersRequest.FromString,
          response_serializer=api__pb2.GetShouldStopWorkersReply.SerializeToString,
      ),
      'GetMetrics': grpc.unary_unary_rpc_method_handler(
          servicer.GetMetrics,
          request_deserializer=api__pb2.GetMetricsRequest.FromString,
          response_serializer=api__pb2.GetMetricsReply.SerializeToString,
      ),
      'SetSuggestionParameters': grpc.unary_unary_rpc_method_handler(
          servicer.SetSuggestionParameters,
          request_deserializer=api__pb2.SetSuggestionParametersRequest.FromString,
          response_serializer=api__pb2.SetSuggestionParametersReply.SerializeToString,
      ),
      'GetSuggestionParameters': grpc.unary_unary_rpc_method_handler(
          servicer.GetSuggestionParameters,
          request_deserializer=api__pb2.GetSuggestionParametersRequest.FromString,
          response_serializer=api__pb2.GetSuggestionParametersReply.SerializeToString,
      ),
      'GetSuggestionParameterList': grpc.unary_unary_rpc_method_handler(
          servicer.GetSuggestionParameterList,
          request_deserializer=api__pb2.GetSuggestionParameterListRequest.FromString,
          response_serializer=api__pb2.GetSuggestionParameterListReply.SerializeToString,
      ),
      'SetEarlyStoppingParameters': grpc.unary_unary_rpc_method_handler(
          servicer.SetEarlyStoppingParameters,
          request_deserializer=api__pb2.SetEarlyStoppingParametersRequest.FromString,
          response_serializer=api__pb2.SetEarlyStoppingParametersReply.SerializeToString,
      ),
      'GetEarlyStoppingParameters': grpc.unary_unary_rpc_method_handler(
          servicer.GetEarlyStoppingParameters,
          request_deserializer=api__pb2.GetEarlyStoppingParametersRequest.FromString,
          response_serializer=api__pb2.GetEarlyStoppingParametersReply.SerializeToString,
      ),
      'SaveStudy': grpc.unary_unary_rpc_method_handler(
          servicer.SaveStudy,
          request_deserializer=api__pb2.SaveStudyRequest.FromString,
          response_serializer=api__pb2.SaveStudyReply.SerializeToString,
      ),
      'SaveModel': grpc.unary_unary_rpc_method_handler(
          servicer.SaveModel,
          request_deserializer=api__pb2.SaveModelRequest.FromString,
          response_serializer=api__pb2.SaveModelReply.SerializeToString,
      ),
      'GetSavedStudies': grpc.unary_unary_rpc_method_handler(
          servicer.GetSavedStudies,
          request_deserializer=api__pb2.GetSavedStudiesRequest.FromString,
          response_serializer=api__pb2.GetSavedStudiesReply.SerializeToString,
      ),
      'GetSavedModels': grpc.unary_unary_rpc_method_handler(
          servicer.GetSavedModels,
          request_deserializer=api__pb2.GetSavedModelsRequest.FromString,
          response_serializer=api__pb2.GetSavedModelsReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.Manager', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class SuggestionStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSuggestions = channel.unary_unary(
        '/api.Suggestion/GetSuggestions',
        request_serializer=api__pb2.GetSuggestionsRequest.SerializeToString,
        response_deserializer=api__pb2.GetSuggestionsReply.FromString,
        )


class SuggestionServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetSuggestions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SuggestionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSuggestions': grpc.unary_unary_rpc_method_handler(
          servicer.GetSuggestions,
          request_deserializer=api__pb2.GetSuggestionsRequest.FromString,
          response_serializer=api__pb2.GetSuggestionsReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.Suggestion', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class EarlyStoppingStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetShouldStopWorkers = channel.unary_unary(
        '/api.EarlyStopping/GetShouldStopWorkers',
        request_serializer=api__pb2.GetShouldStopWorkersRequest.SerializeToString,
        response_deserializer=api__pb2.GetShouldStopWorkersReply.FromString,
        )


class EarlyStoppingServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetShouldStopWorkers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EarlyStoppingServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetShouldStopWorkers': grpc.unary_unary_rpc_method_handler(
          servicer.GetShouldStopWorkers,
          request_deserializer=api__pb2.GetShouldStopWorkersRequest.FromString,
          response_serializer=api__pb2.GetShouldStopWorkersReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.EarlyStopping', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
