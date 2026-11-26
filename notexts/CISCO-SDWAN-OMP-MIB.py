#
# PySNMP MIB module CISCO-SDWAN-OMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SDWAN-OMP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSdwanOmpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 1003))
ciscoSdwanOmpMIB.setRevisions(('2021-03-03 00:00',))
if mibBuilder.loadTexts: ciscoSdwanOmpMIB.setLastUpdated('202103030000Z')
if mibBuilder.loadTexts: ciscoSdwanOmpMIB.setOrganization('Cisco Systems Inc.')
class NotificationSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3))

class OperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("up", 0), ("down", 1))

class PeerState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("invalid", 0), ("init", 1), ("handshake", 2), ("up", 3), ("down", 4), ("init-in-gr", 5), ("down-in-gr", 6), ("handshake-in-gr", 7))

class OmpPolicyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("add", 0), ("delete", 1))

class InetAddressIP(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
ciscoSdwanOmpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1003, 0))
ciscoSdwanOmpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1003, 1))
ciscoSdwanOmpMIBNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2))
ciscoSdwanOmpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1003, 3))
netconfNotificationSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 2), NotificationSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: netconfNotificationSeverity.setStatus('current')
ciscoSdwanOmpNumberOfVsmarts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoSdwanOmpNumberOfVsmarts.setStatus('current')
ciscoSdwanOmpNewState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 4), OperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoSdwanOmpNewState.setStatus('current')
ciscoSdwanOmpPeer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 5), InetAddressIP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoSdwanOmpPeer.setStatus('current')
ciscoSdwanOmpPeerNewState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 6), PeerState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoSdwanOmpPeerNewState.setStatus('current')
ciscoSdwanOmpPolicy = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 7), OmpPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoSdwanOmpPolicy.setStatus('current')
ciscoSdwanOmpVsmartPeer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 8), InetAddressIP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoSdwanOmpVsmartPeer.setStatus('current')
ciscoSdwanOmpOmpNumberOfVsmartsChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 1003, 0, 1)).setObjects(("CISCO-SDWAN-OMP-MIB", "netconfNotificationSeverity"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpNumberOfVsmarts"))
if mibBuilder.loadTexts: ciscoSdwanOmpOmpNumberOfVsmartsChange.setStatus('current')
ciscoSdwanOmpOmpStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 1003, 0, 2)).setObjects(("CISCO-SDWAN-OMP-MIB", "netconfNotificationSeverity"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpNewState"))
if mibBuilder.loadTexts: ciscoSdwanOmpOmpStateChange.setStatus('current')
ciscoSdwanOmpOmpPeerStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 1003, 0, 3)).setObjects(("CISCO-SDWAN-OMP-MIB", "netconfNotificationSeverity"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPeer"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPeerNewState"))
if mibBuilder.loadTexts: ciscoSdwanOmpOmpPeerStateChange.setStatus('current')
ciscoSdwanOmpOmpPolicy = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 1003, 0, 4)).setObjects(("CISCO-SDWAN-OMP-MIB", "netconfNotificationSeverity"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPolicy"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpVsmartPeer"))
if mibBuilder.loadTexts: ciscoSdwanOmpOmpPolicy.setStatus('current')
ciscoSdwanOmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 1))
ciscoSdwanOmpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2))
ciscoSdwanOmpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 1, 1)).setObjects(("CISCO-SDWAN-OMP-MIB", "cSdwanOmpNotifObjsGroup"), ("CISCO-SDWAN-OMP-MIB", "cSdwanOmpNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSdwanOmpMIBCompliance = ciscoSdwanOmpMIBCompliance.setStatus('current')
cSdwanOmpNotifObjsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2, 1)).setObjects(("CISCO-SDWAN-OMP-MIB", "netconfNotificationSeverity"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpNumberOfVsmarts"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpNewState"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPeer"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPeerNewState"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPolicy"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpVsmartPeer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanOmpNotifObjsGroup = cSdwanOmpNotifObjsGroup.setStatus('current')
cSdwanOmpNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2, 2)).setObjects(("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpOmpNumberOfVsmartsChange"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpOmpStateChange"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpOmpPeerStateChange"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpOmpPolicy"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanOmpNotifsGroup = cSdwanOmpNotifsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SDWAN-OMP-MIB", ciscoSdwanOmpVsmartPeer=ciscoSdwanOmpVsmartPeer, netconfNotificationSeverity=netconfNotificationSeverity, OmpPolicyState=OmpPolicyState, PYSNMP_MODULE_ID=ciscoSdwanOmpMIB, ciscoSdwanOmpOmpStateChange=ciscoSdwanOmpOmpStateChange, ciscoSdwanOmpMIBGroups=ciscoSdwanOmpMIBGroups, ciscoSdwanOmpMIBCompliance=ciscoSdwanOmpMIBCompliance, ciscoSdwanOmpPeer=ciscoSdwanOmpPeer, PeerState=PeerState, ciscoSdwanOmpOmpPolicy=ciscoSdwanOmpOmpPolicy, ciscoSdwanOmpMIBNotifs=ciscoSdwanOmpMIBNotifs, OperState=OperState, NotificationSeverity=NotificationSeverity, ciscoSdwanOmpNewState=ciscoSdwanOmpNewState, ciscoSdwanOmpMIB=ciscoSdwanOmpMIB, ciscoSdwanOmpOmpNumberOfVsmartsChange=ciscoSdwanOmpOmpNumberOfVsmartsChange, ciscoSdwanOmpMIBNotifObjects=ciscoSdwanOmpMIBNotifObjects, InetAddressIP=InetAddressIP, cSdwanOmpNotifObjsGroup=cSdwanOmpNotifObjsGroup, ciscoSdwanOmpOmpPeerStateChange=ciscoSdwanOmpOmpPeerStateChange, cSdwanOmpNotifsGroup=cSdwanOmpNotifsGroup, ciscoSdwanOmpMIBConform=ciscoSdwanOmpMIBConform, ciscoSdwanOmpMIBCompliances=ciscoSdwanOmpMIBCompliances, ciscoSdwanOmpPeerNewState=ciscoSdwanOmpPeerNewState, ciscoSdwanOmpPolicy=ciscoSdwanOmpPolicy, ciscoSdwanOmpMIBObjects=ciscoSdwanOmpMIBObjects, ciscoSdwanOmpNumberOfVsmarts=ciscoSdwanOmpNumberOfVsmarts)
