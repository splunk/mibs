#
# PySNMP MIB module CISCO-FC-DEVICE-ALIAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FC-DEVICE-ALIAS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
CdpvmDevType, = mibBuilder.importSymbols("CISCO-DYNAMIC-PORT-VSAN-MIB", "CdpvmDevType")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoFcDeviceAliasMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 430))
ciscoFcDeviceAliasMIB.setRevisions(('2004-09-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFcDeviceAliasMIB.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoFcDeviceAliasMIB.setLastUpdated('200409200000Z')
if mibBuilder.loadTexts: ciscoFcDeviceAliasMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoFcDeviceAliasMIB.setContactInfo('     Cisco Systems\n                      Customer Service\n                Postal: 170 W Tasman Drive\n                      San Jose, CA  95134\n                      USA\n                Tel: +1 800 553 -NETS\n                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoFcDeviceAliasMIB.setDescription('The MIB module for the management of Device\n                 Aliases in a Fibre Channel Fabric. A Fibre\n                 Channel fabric consists of devices such as \n                 disks, hosts and switches. The disks and\n                 hosts login to the switches and avail services\n                 available to them in the fabric.\n                 These devices are identified by means of their\n                 World Wide Names (WWN). The WWNs are 8-byte\n                 cryptic identifiers, which are cumbersome\n                 for human use. \n                 A Device Alias is a human readable string which\n                 can be used to alias a World Wide Name (WWN).\n                 So, a Device Alias is used to map a WWN to\n                 a user friendly name. Once configured, the\n                 Device Alias can be used in place of the\n                 WWN. On the switch, this MIB assists in\n                 defining the Device Aliases for the remote\n                 devices and using these Aliases instead of the\n                 cryptic WWNs.')
cfdaMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 0))
cfdaMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 1))
cfdaMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 2))
cfdaConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1))
cfdaConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1), )
if mibBuilder.loadTexts: cfdaConfigTable.setStatus('current')
if mibBuilder.loadTexts: cfdaConfigTable.setDescription('A table containing information on all\n                 device aliases that have been configured\n                 on the local switch.')
cfdaConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigDeviceAlias"))
if mibBuilder.loadTexts: cfdaConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cfdaConfigEntry.setDescription('Each entry in this table contains the\n                  mapping between the alias for a Fibre Channel\n                  device and its World Wide Name (WWN).')
cfdaConfigDeviceAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: cfdaConfigDeviceAlias.setStatus('current')
if mibBuilder.loadTexts: cfdaConfigDeviceAlias.setDescription('The device alias of this entry. This object\n                 is the human friendly string for the device\n                 represented by the corresponding instance of\n                 cfdaConfigDeviceWwn. A device can have only one\n                 alias configured.\n\n                 The value of this object MUST begin with an\n                 alphabet.')
cfdaConfigDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 2), CdpvmDevType().clone('pwwn')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfdaConfigDeviceType.setStatus('current')
if mibBuilder.loadTexts: cfdaConfigDeviceType.setDescription("The type of the Fibre Channel device represented \n                 by the corresponding instance of \n                 cfdaConfigDeviceId.\n\n                 This object cannot be modified while the value\n                 of the corresponding instance of \n                 cfdaConfigRowStatus is 'active'.")
cfdaConfigDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfdaConfigDeviceId.setStatus('current')
if mibBuilder.loadTexts: cfdaConfigDeviceId.setDescription("The Fibre Channel device which is given a device \n                 alias as indicated by the corresponding instance\n                 of cfdaConfigDeviceAlias. This object MUST be set \n                 to a valid value before or concurrently with \n                 setting the corresponding instance of \n                 cfdaConfigRowStatus object to 'active'. This\n                 object cannot be modified while the value of\n                 the corresponding instance of cfdaConfigRowStatus\n                 object is 'active'.")
cfdaConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfdaConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: cfdaConfigRowStatus.setDescription("The status of this conceptual row.\n                 Before setting this object to 'active', the\n                 corresponding instance of cfdaConfigDeviceId\n                 MUST be set to a valid value.\n                 None of the objects can be modified while the\n                 value of this object is 'active'.")
ciscoFcDaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 1))
ciscoFcDaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 2))
ciscoFcDaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 1, 1)).setObjects(("CISCO-FC-DEVICE-ALIAS-MIB", "ciscoFcDaConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcDaMIBCompliance = ciscoFcDaMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoFcDaMIBCompliance.setDescription('The compliance statement for entities which\n                 implement Device Aliases.')
ciscoFcDaConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 2, 1)).setObjects(("CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigDeviceType"), ("CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigDeviceId"), ("CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcDaConfigGroup = ciscoFcDaConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoFcDaConfigGroup.setDescription('A collection of objects for configuring and\n                 distributing device aliases.')
mibBuilder.exportSymbols("CISCO-FC-DEVICE-ALIAS-MIB", cfdaConfigTable=cfdaConfigTable, cfdaMIBObjects=cfdaMIBObjects, cfdaConfiguration=cfdaConfiguration, PYSNMP_MODULE_ID=ciscoFcDeviceAliasMIB, cfdaMIBNotifs=cfdaMIBNotifs, cfdaConfigDeviceType=cfdaConfigDeviceType, cfdaConfigDeviceId=cfdaConfigDeviceId, ciscoFcDaConfigGroup=ciscoFcDaConfigGroup, cfdaMIBConform=cfdaMIBConform, cfdaConfigEntry=cfdaConfigEntry, cfdaConfigRowStatus=cfdaConfigRowStatus, ciscoFcDaMIBGroups=ciscoFcDaMIBGroups, ciscoFcDaMIBCompliance=ciscoFcDaMIBCompliance, cfdaConfigDeviceAlias=cfdaConfigDeviceAlias, ciscoFcDaMIBCompliances=ciscoFcDaMIBCompliances, ciscoFcDeviceAliasMIB=ciscoFcDeviceAliasMIB)
