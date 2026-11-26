#
# PySNMP MIB module CISCO-IF-CALL-SERVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IF-CALL-SERVICE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
BulkConfigResult, ConfigIterator = mibBuilder.importSymbols("CISCO-TC", "BulkConfigResult", "ConfigIterator")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIfCallServiceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9968))
ciscoIfCallServiceMIB.setRevisions(('2003-04-25 00:00',))
if mibBuilder.loadTexts: ciscoIfCallServiceMIB.setLastUpdated('200304250000Z')
if mibBuilder.loadTexts: ciscoIfCallServiceMIB.setOrganization('Cisco Systems, Inc.')
ciscoIfCallServiceMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 0))
ciscoIfCallServiceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1))
ciscoIfCallServiceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2))
cicServiceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1))
class CIfCallServiceOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inService", 1), ("outOfService", 2), ("oosPending", 3))

class CIfCallServiceAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inService", 1), ("forcedOutOfService", 2), ("gracefulOutOfService", 3))

cicServiceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1), )
if mibBuilder.loadTexts: cicServiceTable.setStatus('current')
cicServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cicServiceEntry.setStatus('current')
cicServiceOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 1), CIfCallServiceOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicServiceOperState.setStatus('current')
cicServiceAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 2), CIfCallServiceAdminState().clone('inService')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceAdminState.setStatus('current')
cicServiceGraceTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceGraceTime.setStatus('current')
cicServiceRepetition = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 4), ConfigIterator().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceRepetition.setStatus('current')
cicServiceRepeatOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 5), OwnerString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceRepeatOwner.setStatus('current')
cicServiceRepeatResult = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 6), BulkConfigResult()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicServiceRepeatResult.setStatus('current')
cicServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 1))
cicServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 2))
cicServiceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 1, 1)).setObjects(("CISCO-IF-CALL-SERVICE-MIB", "cicServiceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicServiceCompliance = cicServiceCompliance.setStatus('current')
cicServiceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 2, 1)).setObjects(("CISCO-IF-CALL-SERVICE-MIB", "cicServiceOperState"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceAdminState"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceGraceTime"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceRepetition"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceRepeatOwner"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceRepeatResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicServiceGroup = cicServiceGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IF-CALL-SERVICE-MIB", cicServiceRepeatResult=cicServiceRepeatResult, cicServiceConfig=cicServiceConfig, CIfCallServiceOperState=CIfCallServiceOperState, cicServiceGraceTime=cicServiceGraceTime, ciscoIfCallServiceMIBNotifs=ciscoIfCallServiceMIBNotifs, cicServiceEntry=cicServiceEntry, cicServiceGroups=cicServiceGroups, cicServiceRepeatOwner=cicServiceRepeatOwner, ciscoIfCallServiceMIB=ciscoIfCallServiceMIB, cicServiceCompliances=cicServiceCompliances, cicServiceTable=cicServiceTable, cicServiceGroup=cicServiceGroup, ciscoIfCallServiceMIBObjects=ciscoIfCallServiceMIBObjects, cicServiceRepetition=cicServiceRepetition, cicServiceAdminState=cicServiceAdminState, PYSNMP_MODULE_ID=ciscoIfCallServiceMIB, cicServiceOperState=cicServiceOperState, ciscoIfCallServiceMIBConformance=ciscoIfCallServiceMIBConformance, CIfCallServiceAdminState=CIfCallServiceAdminState, cicServiceCompliance=cicServiceCompliance)
