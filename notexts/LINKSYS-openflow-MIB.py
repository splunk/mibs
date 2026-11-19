#
# PySNMP MIB module LINKSYS-openflow-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-openflow-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:37:16 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Bits, TimeTicks, NotificationType, MibIdentifier, Counter64, Unsigned32, iso, IpAddress, ObjectIdentity, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "TimeTicks", "NotificationType", "MibIdentifier", "Counter64", "Unsigned32", "iso", "IpAddress", "ObjectIdentity", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, RowStatus, TimeStamp, DisplayString, DateAndTime, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TimeStamp", "DisplayString", "DateAndTime", "TruthValue")
rlOpenFlow = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319))
rlOpenFlowSupported = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowSupported.setStatus('current')
rlOpenFlowTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319, 2), Integer32().clone(6633)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowTcpPort.setStatus('current')
rlOpenFlowServerIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319, 3), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowServerIpAddr.setStatus('current')
rlOpenFlowProtocolType = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("tcp", 0), ("tls", 1))).clone('tcp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowProtocolType.setStatus('current')
rlOpenFlowDefaultForwardAction = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("forward", 0), ("drop", 1), ("toController", 2))).clone('forward')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowDefaultForwardAction.setStatus('current')
rlOpenFlowEnable = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOpenFlowEnable.setStatus('current')
rlOpenFlowEnableAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowEnableAfterReset.setStatus('current')
mibBuilder.exportSymbols("LINKSYS-openflow-MIB", rlOpenFlowSupported=rlOpenFlowSupported, rlOpenFlowTcpPort=rlOpenFlowTcpPort, rlOpenFlowDefaultForwardAction=rlOpenFlowDefaultForwardAction, rlOpenFlow=rlOpenFlow, rlOpenFlowEnableAfterReset=rlOpenFlowEnableAfterReset, rlOpenFlowServerIpAddr=rlOpenFlowServerIpAddr, rlOpenFlowEnable=rlOpenFlowEnable, rlOpenFlowProtocolType=rlOpenFlowProtocolType)
