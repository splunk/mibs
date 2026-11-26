#
# PySNMP MIB module CISCO-VOA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOA-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
OpticalIfDirection, = mibBuilder.importSymbols("CISCO-OPTICAL-MONITOR-MIB", "OpticalIfDirection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
ciscoVoaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 262))
ciscoVoaMIB.setRevisions(('2002-05-07 00:00',))
if mibBuilder.loadTexts: ciscoVoaMIB.setLastUpdated('200205070000Z')
if mibBuilder.loadTexts: ciscoVoaMIB.setOrganization('Cisco Systems, Inc.')
class OpticalPowerInDbm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-400, 250), ValueRangeConstraint(-1000, -1000), )
class OpticalAttenInDb(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 400)

cVoaMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 1))
cVoaBaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1))
cVoaTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1), )
if mibBuilder.loadTexts: cVoaTable.setStatus('current')
cVoaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-VOA-MIB", "cVoaDirection"))
if mibBuilder.loadTexts: cVoaEntry.setStatus('current')
cVoaDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 1), OpticalIfDirection())
if mibBuilder.loadTexts: cVoaDirection.setStatus('current')
cVoaAttenuationControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("automatic", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoaAttenuationControlMode.setStatus('current')
cVoaAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 3), OpticalAttenInDb()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoaAttenuation.setStatus('current')
cVoaAttenuationLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVoaAttenuationLastChange.setStatus('current')
cVoaDesiredPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 5), OpticalPowerInDbm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoaDesiredPower.setStatus('current')
cVoaMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 3))
cVoaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 1))
cVoaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 2))
cVoaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 1, 1)).setObjects(("CISCO-VOA-MIB", "cVoaMIBBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoaMIBCompliance = cVoaMIBCompliance.setStatus('current')
cVoaMIBBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 2, 1)).setObjects(("CISCO-VOA-MIB", "cVoaAttenuationControlMode"), ("CISCO-VOA-MIB", "cVoaAttenuation"), ("CISCO-VOA-MIB", "cVoaAttenuationLastChange"), ("CISCO-VOA-MIB", "cVoaDesiredPower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoaMIBBaseGroup = cVoaMIBBaseGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOA-MIB", PYSNMP_MODULE_ID=ciscoVoaMIB, cVoaMIBGroups=cVoaMIBGroups, OpticalPowerInDbm=OpticalPowerInDbm, cVoaAttenuationLastChange=cVoaAttenuationLastChange, cVoaAttenuationControlMode=cVoaAttenuationControlMode, cVoaMIBObjects=cVoaMIBObjects, OpticalAttenInDb=OpticalAttenInDb, cVoaBaseGroup=cVoaBaseGroup, cVoaAttenuation=cVoaAttenuation, cVoaDesiredPower=cVoaDesiredPower, cVoaTable=cVoaTable, cVoaMIBConformance=cVoaMIBConformance, cVoaMIBCompliances=cVoaMIBCompliances, ciscoVoaMIB=ciscoVoaMIB, cVoaEntry=cVoaEntry, cVoaMIBBaseGroup=cVoaMIBBaseGroup, cVoaMIBCompliance=cVoaMIBCompliance, cVoaDirection=cVoaDirection)
