#
# PySNMP MIB module CISCO-SNMP-VACM-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-VACM-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
vacmSecurityModel, vacmSecurityName = mibBuilder.importSymbols("SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityModel", "vacmSecurityName")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
RowStatus, DisplayString, TextualConvention, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "StorageType")
ciscoSnmpVacmExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 409))
ciscoSnmpVacmExtMIB.setRevisions(('2004-05-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpVacmExtMIB.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoSnmpVacmExtMIB.setLastUpdated('200405190000Z')
if mibBuilder.loadTexts: ciscoSnmpVacmExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpVacmExtMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n                        \n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n                        \n                   Tel: +1 800 553-NETS\n                   \n                E-mail:  cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpVacmExtMIB.setDescription("The management information definitions to extend\n                 the View-based Access Control Model (RFC3415) for\n                 SNMP.\n                 \n                 This MIB extends the 'SNMP-VIEW-BASED-ACM-MIB' to\n                 allow each combination of a 'securityModel' and a\n                 'securityName' to be mapped into additional\n                 groupNames. The groups identified by these mappings\n                 are in addition to those identified by \n                 'vacmGroupName' of the 'vacmSecurityToGroupTable'.\n                 ")
ciscoSnmpVacmExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 1))
ciscoSnmpVacmExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 2))
cvacmSecurityToGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1), )
if mibBuilder.loadTexts: cvacmSecurityToGroupTable.setReference(' [RFC3415] View-based Access Control Model (VACM) for the \n             Simple Network Management Protocol (SNMP), STD 62 .\n           ')
if mibBuilder.loadTexts: cvacmSecurityToGroupTable.setStatus('current')
if mibBuilder.loadTexts: cvacmSecurityToGroupTable.setDescription("An Extension table to the 'vacmSecurityToGroupTable'\n            defined in 'SNMP-VIEW-BASED-ACM-MIB. \n            \n            This table provides a mechanism to map a combination \n            of 'securityModel' and 'securityName' into one or more\n            groups in addition to the 'vacmGroupName' mapped in\n            the 'vacmSecurityToGroupTable'. These groups provide \n            additional access control policies for a principal.\n            \n            The agent must allow the same group mapping entry to be\n            present in both  the 'cvacmSecurityToGroupTable' and the\n            'vacmSecurityToGroupTable'.            \n            \n            A row in this table can not exist without a corresponding\n            row for the same combination of 'securityModel' and\n            'securityName in the 'vacmSecurityToGroupTable'.\n            \n            While creating a row in this table, if there is no\n            corresponding row for the same combination of\n            'securityModel' and 'securityName in the \n            'vacmSecurityToGroupTable', the same  mapping entry in \n            is created in the  'vacmSecurityToGroupTable' by the\n            agent using the values of instance variables of the entry\n            in this table. \n           \n            The deletion of a row in the 'vacmSecurityToGroupTable'\n            also causes the deletion of all the group mapping \n            entries for the same combination of  'vacmSecurityModel' \n            and 'vacmSecurityName' in the 'cvacmSecurityToGroupTable'.\n            The deletion of a row in this table does not affect\n            'vacmSecurityToGroupTable'entries.\n            ")
cvacmSecurityToGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1), ).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityModel"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityName"), (0, "CISCO-SNMP-VACM-EXT-MIB", "cvacmSecurityGrpName"))
if mibBuilder.loadTexts: cvacmSecurityToGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cvacmSecurityToGroupEntry.setDescription("An entry (conceptual row) in the\n            'cvacmSecurityToGroupTable'. Each row represents one\n            groupName mapping for the combination of 'securityModel' \n            and 'securityName' in the system.\n           ")
cvacmSecurityGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cvacmSecurityGrpName.setStatus('current')
if mibBuilder.loadTexts: cvacmSecurityGrpName.setDescription("The name of the group for the mapping represented by\n            this row. This is in addition to the 'vacmGroupName'\n            mapped in the 'vacmSecurityToGroupTable'. For example\n            a user principal  represented by 'securityName' maps\n            to a group represented by 'cvacmSecurityGrpName' under\n            a security model represented by 'securityModel'.\n            \n            This groupName is used as index into the \n            'vacmAccessTable' to select an access control policy.\n            However, a value in this table does not imply that an\n            instance with the value exists in table 'vacmAccesTable'.\n            ")
cvacmSecurityGrpStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1, 2), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvacmSecurityGrpStorageType.setStatus('current')
if mibBuilder.loadTexts: cvacmSecurityGrpStorageType.setDescription("The storage type for this conceptual row.\n            Conceptual rows having the value 'permanent' need not\n            allow write-access to any columnar objects in the row.\n            ")
cvacmSecurityGrpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvacmSecurityGrpStatus.setStatus('current')
if mibBuilder.loadTexts: cvacmSecurityGrpStatus.setDescription('The status of this conceptual row. The value of\n            this object has no effect on whether other objects\n            in this conceptual row can be modified.            \n            ')
ciscoSnmpVacmExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 1))
ciscoSnmpVacmExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 2))
ciscoSnmpVacmExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 1, 1)).setObjects(("CISCO-SNMP-VACM-EXT-MIB", "ciscoSnmpVacmExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmExtMIBCompliance = ciscoSnmpVacmExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpVacmExtMIBCompliance.setDescription('The compliance statement for SNMP engines which \n            implement the CISCO-SNMP-VACM-EXT-MIB.')
ciscoSnmpVacmExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 2, 1)).setObjects(("CISCO-SNMP-VACM-EXT-MIB", "cvacmSecurityGrpStorageType"), ("CISCO-SNMP-VACM-EXT-MIB", "cvacmSecurityGrpStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmExtGroup = ciscoSnmpVacmExtGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpVacmExtGroup.setDescription('A collection of objects providing for remote\n            configuration of an SNMP engine which extends\n            the SNMP View-based Access Control Model.')
mibBuilder.exportSymbols("CISCO-SNMP-VACM-EXT-MIB", ciscoSnmpVacmExtMIBConformance=ciscoSnmpVacmExtMIBConformance, ciscoSnmpVacmExtMIB=ciscoSnmpVacmExtMIB, ciscoSnmpVacmExtMIBObjects=ciscoSnmpVacmExtMIBObjects, PYSNMP_MODULE_ID=ciscoSnmpVacmExtMIB, cvacmSecurityToGroupEntry=cvacmSecurityToGroupEntry, ciscoSnmpVacmExtMIBCompliances=ciscoSnmpVacmExtMIBCompliances, ciscoSnmpVacmExtMIBCompliance=ciscoSnmpVacmExtMIBCompliance, ciscoSnmpVacmExtGroup=ciscoSnmpVacmExtGroup, ciscoSnmpVacmExtMIBGroups=ciscoSnmpVacmExtMIBGroups, cvacmSecurityGrpName=cvacmSecurityGrpName, cvacmSecurityGrpStorageType=cvacmSecurityGrpStorageType, cvacmSecurityGrpStatus=cvacmSecurityGrpStatus, cvacmSecurityToGroupTable=cvacmSecurityToGroupTable)
