#
# PySNMP MIB module CISCO-WAN-TRAP-VARS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-TRAP-VARS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "AutonomousType")
ciscoWanTrapVarsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 5))
ciscoWanTrapVarsMIB.setRevisions(('2002-11-26 00:00', '2002-07-17 00:00', '2001-11-07 00:00', '2001-11-06 00:00', '2001-07-26 00:00', '1999-05-21 00:00',))
if mibBuilder.loadTexts: ciscoWanTrapVarsMIB.setLastUpdated('200211260000Z')
if mibBuilder.loadTexts: ciscoWanTrapVarsMIB.setOrganization('Cisco Systems, Inc.')
cwTrapVarMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 5, 1))
cwTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1))
cwTrapIndex = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapIndex.setStatus('current')
cwTrapSlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapSlotNumber.setStatus('current')
cwTrapPhysicalVendorType = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 3), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapPhysicalVendorType.setStatus('current')
cwTrapLineModuleNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapLineModuleNumber.setStatus('current')
cwTrapOctetString = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapOctetString.setStatus('current')
cwTrapDisplayString = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapDisplayString.setStatus('current')
cwTrapPhysicalContainer = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapPhysicalContainer.setStatus('current')
cwTrapPhysicalUnit = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapPhysicalUnit.setStatus('current')
cwTrapCardRole = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("t1", 1), ("e1", 2), ("t3", 3), ("e3", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapCardRole.setStatus('current')
cwTrapSctCardType = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("axsm", 1), ("axsme", 2), ("pxm1e", 3), ("hsfr", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapSctCardType.setStatus('current')
cwTrapSctType = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("portSct", 1), ("cardSct", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapSctType.setStatus('current')
cwTrapSctId = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapSctId.setStatus('current')
cwTrapSctMajorVersion = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapSctMajorVersion.setStatus('current')
cwTrapVarLength = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapVarLength.setStatus('current')
cwTrapAtmAddressType = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 8))).clone(namedValues=NamedValues(("e164", 3), ("nsap", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapAtmAddressType.setStatus('current')
cwTrapReference = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapReference.setStatus('current')
cwTrapSecondIndex = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapSecondIndex.setStatus('current')
cwTrapThirdIndex = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapThirdIndex.setStatus('current')
cwTrapVarsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 5, 2))
cwTrapVarsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1))
cwTrapVarsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2))
cwTrapVarsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1, 1)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapVarsTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsCompliance = cwTrapVarsCompliance.setStatus('deprecated')
cwTrapVarsCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1, 2)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapVarsTrapGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsCompliance2 = cwTrapVarsCompliance2.setStatus('deprecated')
cwTrapVarsCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1, 3)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapVarsTrapGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsCompliance3 = cwTrapVarsCompliance3.setStatus('deprecated')
cwTrapVarsCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1, 4)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapVarsTrapGroup4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsCompliance4 = cwTrapVarsCompliance4.setStatus('deprecated')
cwTrapVarsCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1, 5)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapVarsTrapGroup5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsCompliance5 = cwTrapVarsCompliance5.setStatus('current')
cwTrapVarsTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2, 1)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapIndex"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSlotNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalVendorType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapLineModuleNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapOctetString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsTrapGroup = cwTrapVarsTrapGroup.setStatus('deprecated')
cwTrapVarsTrapGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2, 2)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapIndex"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSlotNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalVendorType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapLineModuleNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapOctetString"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapDisplayString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsTrapGroup2 = cwTrapVarsTrapGroup2.setStatus('deprecated')
cwTrapVarsTrapGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2, 3)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapIndex"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSlotNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalVendorType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapLineModuleNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapOctetString"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapDisplayString"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalContainer"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalUnit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsTrapGroup3 = cwTrapVarsTrapGroup3.setStatus('deprecated')
cwTrapVarsTrapGroup4 = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2, 4)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapIndex"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSlotNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalVendorType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapLineModuleNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapOctetString"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapDisplayString"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalContainer"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalUnit"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapCardRole"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctCardType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctId"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctMajorVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsTrapGroup4 = cwTrapVarsTrapGroup4.setStatus('deprecated')
cwTrapVarsTrapGroup5 = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2, 5)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapIndex"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSlotNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalVendorType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapLineModuleNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapOctetString"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapDisplayString"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalContainer"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalUnit"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapCardRole"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctCardType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctId"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctMajorVersion"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapVarLength"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapAtmAddressType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapReference"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSecondIndex"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapThirdIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsTrapGroup5 = cwTrapVarsTrapGroup5.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-TRAP-VARS-MIB", cwTrapVarsCompliance5=cwTrapVarsCompliance5, cwTrapVars=cwTrapVars, cwTrapVarsMIBConformance=cwTrapVarsMIBConformance, cwTrapVarsCompliance=cwTrapVarsCompliance, cwTrapVarsTrapGroup5=cwTrapVarsTrapGroup5, cwTrapSlotNumber=cwTrapSlotNumber, cwTrapPhysicalContainer=cwTrapPhysicalContainer, ciscoWanTrapVarsMIB=ciscoWanTrapVarsMIB, cwTrapSctCardType=cwTrapSctCardType, cwTrapOctetString=cwTrapOctetString, cwTrapVarsTrapGroup3=cwTrapVarsTrapGroup3, cwTrapVarsCompliance2=cwTrapVarsCompliance2, cwTrapAtmAddressType=cwTrapAtmAddressType, cwTrapSctId=cwTrapSctId, cwTrapSctMajorVersion=cwTrapSctMajorVersion, cwTrapVarMIBObjects=cwTrapVarMIBObjects, cwTrapThirdIndex=cwTrapThirdIndex, PYSNMP_MODULE_ID=ciscoWanTrapVarsMIB, cwTrapVarsMIBCompliances=cwTrapVarsMIBCompliances, cwTrapVarsTrapGroup2=cwTrapVarsTrapGroup2, cwTrapVarsCompliance3=cwTrapVarsCompliance3, cwTrapVarsCompliance4=cwTrapVarsCompliance4, cwTrapSecondIndex=cwTrapSecondIndex, cwTrapPhysicalVendorType=cwTrapPhysicalVendorType, cwTrapPhysicalUnit=cwTrapPhysicalUnit, cwTrapVarLength=cwTrapVarLength, cwTrapCardRole=cwTrapCardRole, cwTrapVarsTrapGroup4=cwTrapVarsTrapGroup4, cwTrapSctType=cwTrapSctType, cwTrapVarsMIBGroups=cwTrapVarsMIBGroups, cwTrapReference=cwTrapReference, cwTrapVarsTrapGroup=cwTrapVarsTrapGroup, cwTrapIndex=cwTrapIndex, cwTrapLineModuleNumber=cwTrapLineModuleNumber, cwTrapDisplayString=cwTrapDisplayString)
