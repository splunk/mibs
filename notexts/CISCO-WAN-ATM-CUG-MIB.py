#
# PySNMP MIB module CISCO-WAN-ATM-CUG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-ATM-CUG-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
AtmAddr, = mibBuilder.importSymbols("ATM-TC-MIB", "AtmAddr")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoWanAtmCugMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 99999))
ciscoWanAtmCugMIB.setRevisions(('2002-03-22 00:00',))
if mibBuilder.loadTexts: ciscoWanAtmCugMIB.setLastUpdated('200203220000Z')
if mibBuilder.loadTexts: ciscoWanAtmCugMIB.setOrganization('Cisco System Inc.')
cwaCugMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 0))
cwaCugMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1))
cwaCug = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1))
cwaAddressCug = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2))
class CiscoAtmAddressType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 8))
    namedValues = NamedValues(("e164", 3), ("nsap", 8))

class CiscoAtmAddressLength(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 160)

class CiscoAtmInterlockCode(TextualConvention, OctetString):
    reference = 'ATM Forum, Closed User Group, Section 3'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(24, 24)
    fixedLength = 24

cwaCugTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1), )
if mibBuilder.loadTexts: cwaCugTable.setStatus('current')
cwaCugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-ATM-CUG-MIB", "cwaAtmAddress"), (0, "CISCO-WAN-ATM-CUG-MIB", "cwaAddressLength"), (0, "CISCO-WAN-ATM-CUG-MIB", "cwaCugIndex"))
if mibBuilder.loadTexts: cwaCugEntry.setStatus('current')
cwaAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 1), AtmAddr())
if mibBuilder.loadTexts: cwaAtmAddress.setStatus('current')
cwaAddressLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 2), CiscoAtmAddressLength())
if mibBuilder.loadTexts: cwaAddressLength.setStatus('current')
cwaCugIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cwaCugIndex.setStatus('current')
cwaAddressPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 4), CiscoAtmAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaAddressPlan.setStatus('current')
cwaInterlockCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 5), CiscoAtmInterlockCode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaInterlockCode.setStatus('current')
cwaCallsBarred = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("incoming", 2), ("outgoing", 3))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaCallsBarred.setStatus('current')
cwaCugRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaCugRowStatus.setStatus('current')
cwaAddressCugTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1), )
if mibBuilder.loadTexts: cwaAddressCugTable.setStatus('current')
cwaAddressCugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-WAN-ATM-CUG-MIB", "cwaAtmAddress"), (0, "CISCO-WAN-ATM-CUG-MIB", "cwaAddressLength"))
if mibBuilder.loadTexts: cwaAddressCugEntry.setStatus('current')
cwaCugAtmAddressPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 1), CiscoAtmAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwaCugAtmAddressPlan.setStatus('current')
cwaIncomingAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notAllowed", 1), ("allowed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwaIncomingAccess.setStatus('current')
cwaOutgoingAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notAllowed", 1), ("allowedPerCall", 2), ("allowedPermanently", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwaOutgoingAccess.setStatus('current')
cwaPreferentialCug = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwaPreferentialCug.setStatus('current')
ciscoWanAtmCugMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3))
ciscoWanAtmCugMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 1))
ciscoWanAtmCugMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2))
ciscoWanAtmCugMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 1, 1)).setObjects(("CISCO-WAN-ATM-CUG-MIB", "ciscoWanAtmCugGroup"), ("CISCO-WAN-ATM-CUG-MIB", "ciscoWanAtmAddressCugGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmCugMIBCompliance = ciscoWanAtmCugMIBCompliance.setStatus('current')
ciscoWanAtmCugGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2, 1)).setObjects(("CISCO-WAN-ATM-CUG-MIB", "cwaAddressPlan"), ("CISCO-WAN-ATM-CUG-MIB", "cwaInterlockCode"), ("CISCO-WAN-ATM-CUG-MIB", "cwaCallsBarred"), ("CISCO-WAN-ATM-CUG-MIB", "cwaCugRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmCugGroup = ciscoWanAtmCugGroup.setStatus('current')
ciscoWanAtmAddressCugGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2, 2)).setObjects(("CISCO-WAN-ATM-CUG-MIB", "cwaCugAtmAddressPlan"), ("CISCO-WAN-ATM-CUG-MIB", "cwaIncomingAccess"), ("CISCO-WAN-ATM-CUG-MIB", "cwaOutgoingAccess"), ("CISCO-WAN-ATM-CUG-MIB", "cwaPreferentialCug"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmAddressCugGroup = ciscoWanAtmAddressCugGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-ATM-CUG-MIB", CiscoAtmInterlockCode=CiscoAtmInterlockCode, cwaPreferentialCug=cwaPreferentialCug, cwaOutgoingAccess=cwaOutgoingAccess, cwaCugEntry=cwaCugEntry, cwaCugMIBNotifications=cwaCugMIBNotifications, cwaCugAtmAddressPlan=cwaCugAtmAddressPlan, PYSNMP_MODULE_ID=ciscoWanAtmCugMIB, ciscoWanAtmCugMIBCompliances=ciscoWanAtmCugMIBCompliances, cwaIncomingAccess=cwaIncomingAccess, cwaAddressPlan=cwaAddressPlan, cwaCugIndex=cwaCugIndex, ciscoWanAtmCugMIB=ciscoWanAtmCugMIB, cwaAddressCugTable=cwaAddressCugTable, cwaCallsBarred=cwaCallsBarred, cwaCugRowStatus=cwaCugRowStatus, cwaAddressLength=cwaAddressLength, CiscoAtmAddressType=CiscoAtmAddressType, cwaInterlockCode=cwaInterlockCode, ciscoWanAtmCugGroup=ciscoWanAtmCugGroup, cwaAddressCug=cwaAddressCug, ciscoWanAtmAddressCugGroup=ciscoWanAtmAddressCugGroup, cwaAddressCugEntry=cwaAddressCugEntry, cwaAtmAddress=cwaAtmAddress, CiscoAtmAddressLength=CiscoAtmAddressLength, ciscoWanAtmCugMIBConformance=ciscoWanAtmCugMIBConformance, cwaCug=cwaCug, cwaCugTable=cwaCugTable, ciscoWanAtmCugMIBGroups=ciscoWanAtmCugMIBGroups, cwaCugMIBObjects=cwaCugMIBObjects, ciscoWanAtmCugMIBCompliance=ciscoWanAtmCugMIBCompliance)
